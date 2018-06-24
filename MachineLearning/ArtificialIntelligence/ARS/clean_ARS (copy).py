# AI 2018

# Importing the libraries
import os
import numpy as np
import gym
from gym import wrappers
import pybullet_envs

# Setting the Hyper Parameters

class Hp():
    
    def __init__(self):
        self.nb_steps = 1000
        self.episode_length = 1000
        #self.learning_rate = 0.02
        self.learning_rate = 0.1
        self.nb_directions = 16
        self.nb_best_directions = 8
        assert self.nb_best_directions <= self.nb_directions
        self.noise = 0.03
        self.seed = 1
        self.env_name = 'HalfCheetahBulletEnv-v0'
        #self.env_name = 'AntBulletEnv-v0'
        #self.env_name = 'BipedalWalker-v2'
        #self.env_name = 'Hopper-v2'
        
# Normalizing the states

class Normalizer():
    
    def __init__(self, nb_inputs):
        self.n = np.zeros(nb_inputs)
        self.mean = np.zeros(nb_inputs)
        self.mean_diff = np.zeros(nb_inputs)
        self.var = np.zeros(nb_inputs)
    
    def observe(self, x):
        self.n += 1.
        last_mean = self.mean.copy()
        self.mean += (x - self.mean) / self.n
        self.mean_diff += (x - last_mean) * (x - self.mean)
        self.var = (self.mean_diff / self.n).clip(min = 1e-2)
    
    def normalize(self, inputs):
        obs_mean = self.mean
        obs_std = np.sqrt(self.var)
        return (inputs - obs_mean) / obs_std

# Building the AI

class Policy():
    
    def __init__(self, input_size, output_size):
        self.theta = np.zeros((output_size, input_size))
    
    def evaluate(self, input, delta = None, direction = None):
        if direction is None:
            return self.theta.dot(input)
        elif direction == "positive":
            return (self.theta + hp.noise*delta).dot(input)
        else:
            return (self.theta - hp.noise*delta).dot(input)
    
    def sample_deltas(self):
        return [np.random.randn(*self.theta.shape) for _ in range(hp.nb_directions)]
    
    def update(self, rollouts, sigma_r):
        step = np.zeros(self.theta.shape)
        for r_pos, r_neg, d in rollouts:
            step += (r_pos - r_neg) * d
        self.theta += hp.learning_rate / (hp.nb_best_directions * sigma_r) * step

# Exploring the policy on one specific direction and over one episode

def explore(env, normalizer, policy, direction = None, delta = None):
    state = env.reset()
    done = False
    num_plays = 0.
    sum_rewards = 0
    while not done and num_plays < hp.episode_length:
        normalizer.observe(state)
        state = normalizer.normalize(state)
        action = policy.evaluate(state, delta, direction)
        state, reward, done, _ = env.step(action)
        reward = max(min(reward, 1), -1)
        sum_rewards += reward
        num_plays += 1
    return sum_rewards

# Training the AI

def train(env, policy, normalizer, hp):
    
    for step in range(hp.nb_steps):
        
        # Initializing the perturbations deltas and the positive/negative rewards
        deltas = policy.sample_deltas()
        positive_rewards = [0] * hp.nb_directions
        negative_rewards = [0] * hp.nb_directions
        
        # Getting the positive rewards in the positive directions
        for k in range(hp.nb_directions):
            positive_rewards[k] = explore(env, normalizer, policy, direction = "positive", delta = deltas[k])
        
        # Getting the negative rewards in the negative/opposite directions
        for k in range(hp.nb_directions):
            negative_rewards[k] = explore(env, normalizer, policy, direction = "negative", delta = deltas[k])
        
        # Gathering all the positive/negative rewards to compute the standard deviation of these rewards
        all_rewards = np.array(positive_rewards + negative_rewards)
        sigma_r = all_rewards.std()
        
        # Sorting the rollouts by the max(r_pos, r_neg) and selecting the best directions
        scores = {k:max(r_pos, r_neg) for k,(r_pos,r_neg) in enumerate(zip(positive_rewards, negative_rewards))}
        order = sorted(scores.keys(), key = lambda x:scores[x])[:hp.nb_best_directions]
        rollouts = [(positive_rewards[k], negative_rewards[k], deltas[k]) for k in order]
        
        # Updating our policy
        policy.update(rollouts, sigma_r)
        
        # Printing the final reward of the policy after the update
        reward_evaluation = explore(env, normalizer, policy)
        print('Step:', step, 'Reward:', reward_evaluation)

# Running the main code

def mkdir(base, name):
    path = os.path.join(base, name)
    if not os.path.exists(path):
        os.makedirs(path)
    return path
work_dir = mkdir('exp', 'brs')
monitor_dir = mkdir(work_dir, 'monitor')

hp = Hp()
np.random.seed(hp.seed)
env = gym.make(hp.env_name)
env = wrappers.Monitor(env, monitor_dir, force = True)
nb_inputs = env.observation_space.shape[0]
nb_outputs = env.action_space.shape[0]
policy = Policy(nb_inputs, nb_outputs)
normalizer = Normalizer(nb_inputs)
train(env, policy, normalizer, hp)


class MyEnvironment():
    def __init__(self, observation_space, action_space):
        self.observation_space = []
        self.action_space = []
    def step (action):
        y_real = 10
        y_pred = output
        done = False
        info = ''
        reward = 100 / (y_pred - y_real)
        return state, reward, done, info

#from multiprocessing import Pool

#N_int = 10**7  # total iterations
#P_process = 10      # number of processes
    
#pooling = Pool(P_process)
#print(timeit.timeit(lambda: print(f'{sum(p.map(find_pi, [N//P]*P))/P:0.7f}'), number=10))
#pooling.map(train(env, policy, normalizer, hp), [N_int//P_process]*P_process)
#pooling.close()
#pooling.join()
#print(f'{N_int} total iterations with {P_process} processes')   

#(14, -1, False, {'prob': 1.0})
#state, reward, done, info = env.step(1)

# Cheetah core code
#max_episode_steps=1000,
#reward_threshold=4800.0,
#def step(self, action):
#        xposbefore = self.sim.data.qpos[0]
#        self.do_simulation(action, self.frame_skip)
#        xposafter = self.sim.data.qpos[0]
#        ob = self._get_obs()
#        reward_ctrl = - 0.1 * np.square(action).sum()
#        reward_run = (xposafter - xposbefore)/self.dt
#        reward = reward_ctrl + reward_run
#        done = False
#        return ob, reward, done, dict(reward_run=reward_run, reward_ctrl=reward_ctrl)
#
#    def _get_obs(self):
#        return np.concatenate([
#            self.sim.data.qpos.flat[1:],
#            self.sim.data.qvel.flat,
#])

# Ant core code
# max_episode_steps=1000,
# reward_threshold=6000.0,
#def step(self, a):
#        xposbefore = self.get_body_com("torso")[0]
#        self.do_simulation(a, self.frame_skip)
#        xposafter = self.get_body_com("torso")[0]
#        forward_reward = (xposafter - xposbefore)/self.dt
#        ctrl_cost = .5 * np.square(a).sum()
#        contact_cost = 0.5 * 1e-3 * np.sum(
#            np.square(np.clip(self.sim.data.cfrc_ext, -1, 1)))
#        survive_reward = 1.0
#        reward = forward_reward - ctrl_cost - contact_cost + survive_reward
#        state = self.state_vector()
#        notdone = np.isfinite(state).all() \
#            and state[2] >= 0.2 and state[2] <= 1.0
#        done = not notdone
#        ob = self._get_obs()
#        return ob, reward, done, dict(
#            reward_forward=forward_reward,
#            reward_ctrl=-ctrl_cost,
#            reward_contact=-contact_cost,
#reward_survive=survive_reward)
# Augmented Random Search
# Import libraries
import os # Operational System
import numpy as np
import gym
from gym import wrappers
import pybullet_envs

# Setting the Hyper Parameters
class HyperParameters():
    def __init__(self):
        self.nb_steps = 1000 # Number of loops
        self.episode_lenght = 1000 # Maximum time of each Episode
        self.learning_rate = 0.02 # How fast the AI learns
        self.nb_directions = 16 # Number of perturbations sampled from Gaussian Distributions
                                # we will aply on each of the weights
        self.nb_best_directions = 16 # Number of directions left after choosing 
                                     # best perturbations from Rewards
        assert self.nb_best_directions <= self.nb_directions
        self.noise = 0.03 # Perturbations Guassian distributions Std Deviation
        self.seed = 1 # To equalize results in different sessions
        self.env_name = 'HalfCheetahBulletEnv-v0' # Name of the environment
        
# Normalizing the states: the Neural Network will make a much better results of values between 
# 0 and 1 than between any other numbers (0 and 100 for example)
class Normalizer():
    def __init__(self, nb_inputs):
        self.n = np.zeros(nb_inputs) # Counter - Vector of nb_inputs values initialized with zeros
        self.mean = np.zeros(nb_inputs) # Vector of nb_inputs values initialized with zeros
        self.mean_diff = np.zeros(nb_inputs) # Vector of nb_inputs values initialized with zeros
        self.variance = np.zeros(nb_inputs) # Vector of nb_inputs values initialized with zeros
        
        # Observe new state x and online compute mean and variance
    def observe(self, x):
        self.n += 1. # Count new state (float)
        # Online computation of the new Mean:
        last_mean = self.mean.copy()
        self.mean += (x - self.mean) / self.n
        # Online computation of the new Variance
        self.mean_diff += (x - last_mean) * (x - self.mean) # Numerator
        self.variance = (self.mean_diff / self.n).clip(min = 1e-2) # Variance, can't be one (clip to 0.01)
    
    def normalize(self, inputs):
        obs_mean = self.mean # Observed mean
        obs_std_dev = np.sqrt(self.variance) # Observed Std Deviation
        return (inputs - obs_mean ) / obs_std_dev # Return the normalized Inputs
        
# Building the AI
class Policy():
    def __init__ (self, input_size, output_size):
        self.theta = np.zeros((output_size, input_size)) # Matrix of Weights of the Perceptron
                                                         # of the Policy (AI), with output_size
                                                         # lines and input_size columns
        
        # Aply Perturbations in the Positive and Negative directions to each of the Weights
    def evaluate(self, input, delta = None, direction = None): # delta is the Perturbations, 
                                                               # following a Normal (Gaussian) 
                                                               # Distribution of very small numbers
        if direction is None: # No Perturbation
            return self.theta.dot(input) # Aplying the Matrix of Weights Theta to the Input state Vector
        elif direction == 'positive': # Positive Perturbation
            return (self.theta + (hp.noise * delta)).dot(input) # Adding POSITIVE Perturbation 
                                                                # to the Matrix of Weights Theta and 
                                                                # then aplying to the Input state Vector
        else: # Negative Perturbation
            return (self.theta - (hp.noise * delta)).dot(input) # Adding NEGATIVE Perturbation to the
                                                                # Matrix of Weights Theta and then aplying 
                                                                # to the Input state Vector

     # Sampling Perturbations deltas Matrix of the same dimensions of Matrix theta
     # using Normal (Gaussian) Distributions
    def sample_deltas (self):
        return [np.random.randn(*self.theta.shape) for i in range(hp.nb_directions)] # Create 16 Matrices 
                                                                                     # of small random values
                                                                                     # following a Normal (Gaussian)
                                                                                     # Distribution of mean
                                                                                     # 0 and variance 1
    
    # Method of Finite Differences - Aproximation of Gradient Descent 
    def update (self, rollouts, sigma_r): # sigma_r is the Std Deviation of the Reward 
                                        # rollout is a list of several triples: the REWARD of the Positive direction, 
                                        # the REWARD of the negative direction, 
                                        # the perturbation that obtained these REWARDS
        step = np.zeros(self.theta.shape)
        for reward_pos, reward_neg, perturbation in rollouts: # Loop through all the Rewards obtained in the
                                                              # positive and negative direction
            step += (reward_pos - reward_neg) * perturbation
        self.theta += hp.learning_rate / (hp.nb_best_directions * sigma_r) * step #  Update the matrix of Weights in
                                                                                  # the direction that increases
                                                                                  # the most the Reward

# Exploring the Policy on one specific direction and over one Episode 
def explore(env, normalizer, policy, direction = None, delta = None): # env is the environment
    state = env.reset() # Reset the environment
    done = False # Dummy variable to finish the Episode
    num_plays = 0. # Number of action plays for this Episode
    sum_rewards = 0 # Total sum of REWARDS on this direction on this Episode
    while not done and num_plays < hp.episode_lenght: # While we haven't reached the end of the Episode and the
                                                      # number of actions played is lower than the Episode lenght,
                                                      # we compute the accumulated REWARD on the full Episode
        normalizer.observe(state) # Normalize the Input and observe the state (get mean and variance)
        state = normalizer.normalize(state) # Get the normalized state
        action = policy.evaluate(state, delta, direction) # Feed the state to the Perceptron in a direction 
                                                          # with a delta and returns the played action
        state, reward, done, _ = env.step(action) # Takes action played and return the state, reward and done 
                                                  # using the step method of Pybullet
        reward = max(min(reward, 1), -1) # Transform all high values to either +1 or -1
        sum_rewards += reward # Add reward to the sum
        num_plays += 1 # Count +1 play
    return sum_rewards

# Train the AI
def train (env, policy, normalizer, hp):
    for step in range(hp.nb_steps): # loop through 0 to total number of steps (1000)

    # Sample and initialize the Perturbations deltas and the positive and negative REWARDS
        deltas = policy.sample_deltas()
        positive_rewards = [0] * hp.nb_directions # List of 16 zeros
        negative_rewards = [0] * hp.nb_directions # List of 16 zeros
    # Getting the REWARDS by aplying perturbations in the k'th positive directions
        for k in range(hp.nb_directions): # For each direction, update the list of REWARDS
            positive_rewards[k] = explore(env, normalizer, policy, direction = 'positive', delta = deltas[k])
    # Getting the REWARDS by aplying perturbations in the k'th negative directions
        for k in range(hp.nb_directions): # For each direction, update the list of REWARDS
            negative_rewards[k] = explore(env, normalizer, policy, direction = 'negative', delta = deltas[k])
    # Gathering all the positve/negative REWARDS to compute the Std Deviation of these REWARDS
        all_rewards = np.array(positive_rewards + negative_rewards)
        sigma_r = all_rewards.std() # Calculate the Std Deviation of all the values of all the REWARDS
    # Sorting the rollouts by the max between positive and negative in a direction and selecting the best directions
        # Create a dictionary of maximum of the 16 REWARDS in pos and neg
        scores = {k:max(reward_pos, reward_neg) for k, (reward_pos, reward_neg) in enumerate(zip(positive_rewards, negative_rewards))} 
        order = sorted(scores.keys(), key = lambda x:scores)[:hp.nb_best_directions] # Sort the scores dictionary by the maximum 
                                                                                  # that are the REWARDs in the positive and
                                                                                  # negative directions 
                                                                                  # for the 16 dfferent directions, and return 
                                                                                  # the keys of the Dicionary up to the number of
                                                                                  # best directions
        rollouts = [(positive_rewards[k], negative_rewards[k], deltas[k]) for k in order]
    # Update the Policy
        policy.update(rollouts, sigma_r)

    # Printing the final REWARD of the Policy after the Update
        reward_evaluation = explore(env, normalizer, policy)
        print('Step', step, 'Reward: ', reward_evaluation)

# Running the main code

# Create directory for videos of AI running
def mkdir(base, name):
    path = os.path.join(base, name)
    if not os.path.exists(path):
        os.makedirs(path)
    return path
work_dir = mkdir('exp', 'brs')
monitor_dir = mkdir(work_dir, 'monitor')

# Create objects and initialize
hp = HyperParameters() # Hyperparameters object
np.random.seed(hp.seed) # Seed the random values to get same results of lectures
env = gym.make(hp.env_name) # Connect the AI to the environment through Gym
env = wrappers.Monitor(env, monitor_dir, force = True) # Visualise the videos of AI walking
nb_inputs = env.observation_space.shape[0]  # Take the inputs of the specific environment
nb_outputs = env.action_space.shape[0]      # Take the outputs of the specific environment
policy = Policy(nb_inputs, nb_outputs)      # Create the policy object
normalizer = Normalizer(nb_inputs)          # Create the normalizer object
train(env, policy, normalizer, hp)          # Start the program! Train the AI!












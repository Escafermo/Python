def pig_word(word):
	first_letter = word[0]

	if first_letter in 'aeiou':
		pig_word = word + 'ay'
	else:
		pig_word = word[1:] + first_letter + 'ay'
	return pig_word.lower()

word = input('Convert to pig language: ' )
print(pig_word(word))
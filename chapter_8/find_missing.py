# Answer to exercise 3 in chapter 8 
#
# Exercise from: A Common-Sense Guide to Data Structures and Algorithms 
# Level Up Your Core Programming Skills 
# by Jay Wengrow and edited by Brian MacDonald

import sys

def find_missing_char(phrase):
	"""find missing letter from the alphabet in str:phrase"""
	phrase = str(phrase).lower()
	char_map = {chr(key):0 for key in range(97,123)}
	missing_char = ''

	for char in phrase: 
		char_map[char] = char_map.get(char) + 1

	for char, number in char_map.items():
		if number == 0:
			missing_char = char
			print(f"Missing char '{char}'")
			break

	return missing_char

if __name__ == "__main__":
	# example usage: 
        # $python find_missing.py thequickbrownboxjumpsoveralazydog 
	# -> Missing char 'f'
        # argv[1] is a string 
	find_missing_char(sys.argv[1])

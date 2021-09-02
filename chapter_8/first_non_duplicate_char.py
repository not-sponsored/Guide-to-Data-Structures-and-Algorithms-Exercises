# Answer to exercise 4 in chapter 8 
#
# Exercise from: A Common-Sense Guide to Data Structures and Algorithms 
# Level Up Your Core Programming Skills 
# by Jay Wengrow and edited by Brian MacDonald

import sys

def find_first_non_duplicate_char(word: str):
	"""find the first non duplicate char from str:word"""
	map = {} 
	first_non_duplicate = ''

	for char in word:
		map[char] = map.get(char, 0) + 1

	for char, count in map.items():
		if count == 1:
			first_non_duplicate = char
			print(f"First non-duplicate character is '{char}'")
			break;

	return first_non_duplicate 

if __name__ == "__main__":
	# example usage:
	# $python first_non_duplicate_char.py minimum
	# -> First non-duplicate character is 'n' 
        # argv[1] is a string 
	find_first_non_duplicate_char(sys.argv[1])

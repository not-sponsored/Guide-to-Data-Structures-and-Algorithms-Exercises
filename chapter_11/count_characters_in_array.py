# Answer to exercise 1 in chapter 11 
#
# Exercise from: A Common-Sense Guide to Data Structures and Algorithms 
# Level Up Your Core Programming Skills 
# by Jay Wengrow and edited by Brian MacDonald

import sys

def count_characters(array: list):
	"""given a list:array of strings return the character count""" 
	if len(array) == 1:           # base case
		return len(array[0])	
	elif len(array) == 0:         # edge case of empty array
		return 0 
	else:
		return len(array[0]) + count_characters(array[1:])

def main(array: str):
	print(f'Total characters in the array: {count_characters(array)}')

if __name__ == '__main__':
	# example usage:
        # $python count_characters_in_array.py ab,c,def,ghij 
        # -> Total characters in the array: 10 
        # argv[1] is a list of characters separated by commas with no spaces
	main(str(sys.argv[1]).split(','))

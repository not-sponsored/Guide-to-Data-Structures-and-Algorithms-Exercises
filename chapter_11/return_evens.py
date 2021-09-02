# Answer to exercise 2 in chapter 11 
#
# Exercise from: A Common-Sense Guide to Data Structures and Algorithms 
# Level Up Your Core Programming Skills 
# by Jay Wengrow and edited by Brian MacDonald

import sys

def return_evens(array: list):
	"""given an array of ints return only the even ints"""
	if len(array) == 1:
		if array[0] % 2 == 0:
			return [array[0]]
		else:
			return []
	elif len(array) == 0:  # empty array edge case
		return []
	else:
		if array[0] % 2 == 0:
			return [array[0]] + return_evens(array[1:])
		else:
			return return_evens(array[1:])

def main(array: str):
	print(f'Evens are: {return_evens([int(x) for x in array.split(",")])}')

if __name__ == '__main__':
	# example usage:
        # $python return_evens.py 5,2,3,7,6
        # -> Evens are: [2, 6] 
        # argv[1] is a list of numbers separated by commas with no spaces
	main(sys.argv[1])

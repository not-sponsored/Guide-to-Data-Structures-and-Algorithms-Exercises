# Answer to exercise 1 in chapter 12 
#
# Exercise/code from: A Common-Sense Guide to Data Structures and Algorithms 
# Level Up Your Core Programming Skills 
# by Jay Wengrow and edited by Brian MacDonald

import sys

def add_until_100(array: list):
	"""add numbers to a sum from list: array unless makes sum > 100"""
	if not array:    # base case
		return 0
	sum_remaining = add_until_100(array[1:])
	if array[0] + sum_remaining > 100:
		return sum_remaining
	else:
		return array[0] + sum_remaining 

def main(array: list):
	print(f'Adding up to 100: {add_until_100(array)}')

if __name__ == '__main__':
	# example usage:
        # $python add_until_100.py 5,2,3,7,97
        # -> Adding up to 100: 100 
        # argv[1] is a list of numbers separated by commas with no spaces
	main([int(x) for x in sys.argv[1].split(',')])

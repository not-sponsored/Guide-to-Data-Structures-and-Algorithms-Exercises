# Answer to exercise 2 in chapter 20 
#
# Exercise from: A Common-Sense Guide to Data Structures and Algorithms 
# Level Up Your Core Programming Skills 
# by Jay Wengrow and edited by Brian MacDonald

import sys

def missing_int(array: list): 
	"""given array return the missing integer in the continuous sequence
	the following algorithm provides the missing integer in O(N) time
	"""
	full_sum = (len(array) + 1) * len(array) / 2
	array_sum = sum(array) 
	return int(full_sum - array_sum) 

def main(array):
	print(f'Missing int in the consecutive sequence: {array}')
	print(f'is {missing_int(array)}')

if __name__ == "__main__":
        # example usage:
	# $python missing_integer.py 0,1,2,4 
	# -> Missing int in the consecutive sequence: [0, 1, 2, 4]
	# -> is 3
	# argv[1] is a list of numbers separated by commas with no spaces 
	main([int(x) for x in sys.argv[1].split(',')])

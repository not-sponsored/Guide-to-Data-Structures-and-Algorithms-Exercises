# Answer to exercise 3 in chapter 19 
#
# Exercise from: A Common-Sense Guide to Data Structures and Algorithms 
# Level Up Your Core Programming Skills 
# by Jay Wengrow and edited by Brian MacDonald

import sys
import math

def reverse_array(array: list): 
	"""given an array reverse the array in place or with O(1) space"""
	length = len(array)

	# only swap to halfway point
	for index in range(0, math.floor(length / 2)): 
		swap_index = length - (index + 1)
		array[index],array[swap_index] = array[swap_index],array[index]

	return array

def main(array: list):
	print(f'Array to reverse in constant space is: {array}')
	print(f'Reversed: {reverse_array(array)}')	

if __name__ == "__main__":
        # example usage:
	# $python constant_space_reverse.py 5,2,3,7
	# -> Array to reverse in constant space is: [5, 2, 3, 7]
	# -> Reversed: [7, 3, 2, 5]
	# argv[1] is a list of numbers separated by commas with no spaces 
	main([int(x) for x in sys.argv[1].split(',')])

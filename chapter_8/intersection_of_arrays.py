# Answer to exercise 1 in chapter 8 
#
# Exercise from: A Common-Sense Guide to Data Structures and Algorithms 
# Level Up Your Core Programming Skills 
# by Jay Wengrow and edited by Brian MacDonald

import sys

def find_array_intersection(first: list, second: list):
	"""find and return intersection between the integer lists""" 
	first= [int(x) for x in first.split(',')]
	second= [int(x) for x in second.split(',')]

	map = {number:True for number in first}
	intersection = [number for number in second if number in map]

	print(f'The intersection of the arrays is {intersection}')
	return intersection

if __name__ == "__main__":
	# example usage:
	# $python intersection_of_arrays.py 1,2,3 2,3,4 
	# -> The intersection of the arrays is [2, 3]
        # both args are a list of numbers separated by commas with no spaces
	find_array_intersection(sys.argv[1], sys.argv[2])

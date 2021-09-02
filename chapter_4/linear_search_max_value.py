# Answer to exercise 4 in chapter 4
#
# Exercise from: A Common-Sense Guide to Data Structures and Algorithms 
# Level Up Your Core Programming Skills 
# by Jay Wengrow and edited by Brian MacDonald

import sys

def linear_search(unparsed_array: list):
	"""given unparsed_array find the maximum value in O(N) time"""
	array = [int(x) for x in unparsed_array.split(',')]
	greatest = array[0]
	for number in array[1:]:        # first value already set as greatest
		if number > greatest:
			greatest = number 
	print(f'Greatest number: {greatest}')
	return greatest

if __name__ == "__main__":
        # example usage:
	# $python linear_search_max_value.py 5,2,3,7
	# -> Greatest number: 7
	# argv[1] is a list of numbers separated by commas with no spaces 
	linear_search(sys.argv[1])

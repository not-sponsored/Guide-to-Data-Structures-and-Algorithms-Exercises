# Answer to exercise 4 in chapter 10 
#
# Exercise from: A Common-Sense Guide to Data Structures and Algorithms 
# Level Up Your Core Programming Skills 
# by Jay Wengrow and edited by Brian MacDonald

import sys

test_array = [
1,
2,
3,
[4, 5, 6],
7,
[8,
[9, 10, 11,
[12, 13, 14]
]
],
[15, 16, 17, 18, 19,
[20, 21, 22,
[23, 24, 25,
[26, 27, 29]
], 30, 31
], 32
], 33
]

def print_flattened_array(array: list=test_array):
	"""given list:array print out the flattened array (only ints)"""
	for number in array:
		if isinstance(number, list):
			print_flattened_array(number)
		else:
			print(number, end=' ')
	return

if __name__ == '__main__':
	# example usage:
        # $python print_flattened_array.py
        # -> 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
        # -> 26 27 29 30 31 32 33  
        # argv[1] is a nested list of numbers separated by commas with no spaces
	if len(sys.argv) > 1:
		print_flattened_array(sys.argv[1])
	print_flattened_array()

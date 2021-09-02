# Answer to exercise 2 in chapter 13 
#
# Exercise/code from: A Common-Sense Guide to Data Structures and Algorithms 
# Level Up Your Core Programming Skills 
# by Jay Wengrow and edited by Brian MacDonald

import sys

def find_missing_number(array: list):
	"""return the missing number in the continuous integer sequence"""
	array.sort()
	missing = 0
	for index, number in enumerate(array):
		if index != number:
			missing = index
			print(f'Missing from the continuous sequence: {index}')
			break
	return missing

if __name__ == '__main__':
	# example usage:
        # $python missing_number.py 0,1,2,4,5 
        # -> Missing from the continuous sequence: 3
        # argv[1] is a list of numbers separated by commas with no spaces
	find_missing_number([int(x) for x in sys.argv[1].split(',')])

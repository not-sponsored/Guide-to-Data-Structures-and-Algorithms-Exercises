# Answer to exercise 1 in chapter 13 
#
# Exercise from: A Common-Sense Guide to Data Structures and Algorithms 
# Level Up Your Core Programming Skills 
# by Jay Wengrow and edited by Brian MacDonald

import sys

def greatest_product(array: list):
	"""return greatest product of three numbers given positive numbers""" 
	greatest_product = None
	array.sort()
	if len(array) >= 3:
		greatest_product = array[-1] * array[-2] * array[-3]
		print(f'Greatest product of three numbers: {greatest_product}')
	else:
		print('Not enough elements')
	return greatest_product

if __name__ == '__main__':
	# example usage:
        # $python greatest_product.py 5,2,3,7
        # -> Greatest product of three numbers: 105
        # argv[1] is a list of numbers separated by commas with no spaces
	greatest_product([int(x) for x in sys.argv[1].split(',')])

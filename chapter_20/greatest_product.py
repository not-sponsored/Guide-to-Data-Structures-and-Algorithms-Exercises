# Answer to exercise 4 in chapter 20 
#
# Exercise from: A Common-Sense Guide to Data Structures and Algorithms 
# Level Up Your Core Programming Skills 
# by Jay Wengrow and edited by Brian MacDonald

import sys

def greatest_product(array: list): 
	"""given array return the greatest product possible in O(N)"""
	if len(array) < 2:
		return None  # error we need at least two for product
	elif len(array) == 2:
		return array[0] * array[1]  # only option

	greatest = 0
	second_greatest = 0
	least = 0
	second_least = 0

	for number in array:
		if number > greatest:
			second_greatest = greatest
			greatest = number
		elif number > second_greatest:
			second_greatest = number

		if number < least:
			second_least = least
			least = number
		elif number < second_least:
			second_least = number

	if least * second_least > greatest * second_greatest:
		return least * second_least
	return greatest * second_greatest
		
def main(array: list):
	print(f'Greatest product in: {array}')
	print(f'is {greatest_product(array)}')

if __name__ == "__main__":
        # example usage:
	# $python greatest_product.py -1,-2,1,2,4 
	# -> Greatest product in: [-1, -2, 1, 2, 4]
	# -> is 8 
	# argv[1] is a list of numbers separated by commas with no spaces 
	main([int(x) for x in sys.argv[1].split(',')])

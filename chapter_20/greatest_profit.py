# Answer to exercise 3 in chapter 20 
#
# Exercise from: A Common-Sense Guide to Data Structures and Algorithms 
# Level Up Your Core Programming Skills 
# by Jay Wengrow and edited by Brian MacDonald

import sys

def greatest_profit(array: list): 
	"""given array return the maximum profit from one buy and sell
	the following algorithm does so in O(N) time
	"""	
	minimum_price = array[0]
	maximum_price = array[0]
	greatest_profit = 0

	for price in array:
		if price < minimum_price:
			minimum_price = price
			maximum_price = price
		
		if price > maximum_price:
			maximum_price = price

		if maximum_price - minimum_price  > greatest_profit:
			greatest_profit = maximum_price - minimum_price 
	return greatest_profit

def main(array):
	print(f'Greatest profit for single buy and sell of: {array}')
	print(f'is ${greatest_profit(array)}')

if __name__ == "__main__":
        # example usage:
	# $python greatest_profit.py 85,50,48,78,38 
	# -> Greatest profit for single buy and sell of: [85, 50, 48, 78, 38]
	# -> is $30
	# argv[1] is a list of numbers separated by commas with no spaces 
	main([int(x) for x in sys.argv[1].split(',')])

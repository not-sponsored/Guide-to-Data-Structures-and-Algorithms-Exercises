# Answer to exercise 3 in chapter 10 
#
# Exercise from: A Common-Sense Guide to Data Structures and Algorithms 
# Level Up Your Core Programming Skills 
# by Jay Wengrow and edited by Brian MacDonald

import sys

def sum_range(low: int, high: int):
	"""sum the range between low and high (inclusive) with recursion"""
	if low == high:
		return low
	return high + sum_range(low, high - 1)

def main(low: str, high: str):
	print(f'The sum of the range is {sum_range(int(low), int(high))}')

if __name__ == '__main__':
	# example usage:
        # $python sum_range.py 10 55 
        # -> The sum of the range is 1495  
        # argv[1] is a list of numbers separated by commas with no spaces
	main(sys.argv[1], sys.argv[2])

# Answer to exercise 3 in chapter 12 
#
# Exercise/code from: A Common-Sense Guide to Data Structures and Algorithms 
# Level Up Your Core Programming Skills 
# by Jay Wengrow and edited by Brian MacDonald

import sys

def number_unique(row: int, col: int, map={}):
	"""Memoized unique shortest paths solution"""
	if row == 1 or col == 1:
		return 1
	elif (row, col) not in map:
		map[(row, col)] = number_unique(row - 1, col, map)\
				  + number_unique(row, col - 1, map)
	return map[(row, col)]

def main(row: int, col: int):
	print(f'Number of unique shortest paths: {number_unique(row, col)}')

if __name__ == '__main__':
	# example usage:
        # $python memoized_unique_paths.py 3 3 
        # -> Number of unique shortest paths: 6 
        # argv[1] is a int of rows and argv[2] is an int of columns 
	main(int(sys.argv[1]), int(sys.argv[2]))

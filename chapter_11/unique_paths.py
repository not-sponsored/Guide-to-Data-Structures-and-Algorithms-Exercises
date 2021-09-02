# Answer to exercise 5 in chapter 11 
#
# Exercise from: A Common-Sense Guide to Data Structures and Algorithms 
# Level Up Your Core Programming Skills 
# by Jay Wengrow and edited by Brian MacDonald
#
# A much faster memoized version is included in
# chapter_12/memoized_unique_paths.py 

import sys

def number_unique(row: int, column: int):
	"""return number of unique shortest paths from start to finish""" 
	if row == 1 or column == 1:        # base case
		return 1
	else:
		return number_unique(row - 1, column)\
		       + number_unique(row, column - 1) 

def main(row: str, col: str):
	print(f'Paths for {row}x{col}: {number_unique(int(row), int(col))}')

if __name__ == '__main__':
	# example usage:
        # $python unique_paths.py 3 3
        # -> Paths for 3x3: 6 
        # argv[1] int for rows and argv[2] is an int for columns 
	main(sys.argv[1], sys.argv[2])

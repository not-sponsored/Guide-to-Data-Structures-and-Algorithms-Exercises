# Answer to exercise 3 in chapter 11 
#
# Exercise from: A Common-Sense Guide to Data Structures and Algorithms 
# Level Up Your Core Programming Skills 
# by Jay Wengrow and edited by Brian MacDonald

import sys

def triangular_sequence(position: int):
	"""return the nth number in the triangle sequence""" 
	if position == 1:    # base case
		return 1 
	elif position <= 0:  # edge case
		print(f'Invalid input: {position}')
	else:
		return position +  triangular_sequence(position - 1)

def main(number: str):
	print(f'Value at {number} is {triangular_sequence(int(number))}')

if __name__ == '__main__':
	# example usage:
        # $python triangular_numbers.py 7 
        # -> Value at 7 is 28
        # argv[1] is a integer position of the sequence 
	main(sys.argv[1])

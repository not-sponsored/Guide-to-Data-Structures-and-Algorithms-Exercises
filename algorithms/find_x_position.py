# Answer to exercise 4 in chapter 11 
#
# Exercise from: A Common-Sense Guide to Data Structures and Algorithms 
# Level Up Your Core Programming Skills 
# by Jay Wengrow and edited by Brian MacDonald

import sys

def index_of_x(word: str, position=0):
	"""return the index of the first 'x' character"""
	if word[position] == 'x': 
		return position 
	else:
		return index_of_x(word, position + 1) 

def main(word):
	print(f"First 'x' character at {index_of_x(str(word).lower())}")

if __name__ == '__main__':
	# example usage:
        # $python find_x_position.py findxherexthere 
        # -> First 'x' character at 4 
        # argv[1] is a string with 'x' in it 
	main(sys.argv[1])

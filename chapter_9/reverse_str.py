# Answer to exercise 4 in chapter 9 
#
# Exercise from: A Common-Sense Guide to Data Structures and Algorithms 
# Level Up Your Core Programming Skills 
# by Jay Wengrow and edited by Brian MacDonald

from collections import deque
import sys

def reverse_string(word: str):
	"""reverse str:word with a stack"""
	reversed = ''
	stack = deque(str(word).lower())

	while stack: 
		reversed += stack.pop()

	print(f'reversed: {reversed}')
	return reversed

if __name__ == "__main__":
	# example usage:
	# $python reverse_str.py stack
	# -> reversed: kcats 
        # argv[1] is a string
	reverse_string(sys.argv[1])

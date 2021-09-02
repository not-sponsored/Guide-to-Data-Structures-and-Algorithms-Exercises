# Answer to exercise 4 in chapter 6 
#
# Exercise/code from: A Common-Sense Guide to Data Structures and Algorithms 
# Level Up Your Core Programming Skills 
# by Jay Wengrow and edited by Brian MacDonald

import sys

def find_x(search_string):
	"""find x in the search str:arr; return True if found""" 
	found = False
	for char in search_string:
		if char.lower() == 'x':
			found = True
			break
	print(f'Is x in the string? {found}')
	return found 

if __name__ == "__main__":
	# example usage:
	# $python is_x_in_str.py thereisXinthisstring 
	# -> Is x in the string? True 
        # argv[1] is a string 
	find_x(sys.argv[1])

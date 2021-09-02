# Answer to exercise 2 in chapter 8 
#
# Exercise from: A Common-Sense Guide to Data Structures and Algorithms 
# Level Up Your Core Programming Skills 
# by Jay Wengrow and edited by Brian MacDonald

from collections import defaultdict
import sys

def find_duplicate(strings: list):
	"""find the first duplicate string from list:strings"""
	strings = [str(x) for x in strings.split(',')]
	map = defaultdict(int) 
	duplicate_string = ''

	for word in strings:
		if map[word]:
			duplicate_string = word
			print(f'The duplicate string is "{word}"')
			break
		else:
			map[word] += 1

	return duplicate_string

if __name__ == "__main__":
	# example usage:
	# $python find_duplicate_str.py a,b,c,d,a,e,f
	# -> The duplicate string is "a"
        # argv[1] is a list of strings separated by commas with no spaces
	find_duplicate(sys.argv[1])

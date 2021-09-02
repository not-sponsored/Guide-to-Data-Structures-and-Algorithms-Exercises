# Answer to exercise 6 in chapter 20 
#
# Exercise from: A Common-Sense Guide to Data Structures and Algorithms 
# Level Up Your Core Programming Skills 
# by Jay Wengrow and edited by Brian MacDonald

import sys

def get_longest_consecutive_sequence(array: list): 
	"""given array return longest consecutive sequence length
	the following algorithm provides the length in O(N) time
	"""
	if len(array) < 1:
		return 0
	hashmap = {number: True for number in array}
	longest_consecutive = 1                      # array must have a value 

	while hashmap: 
		key = next(iter(hashmap.keys())) 
		distance_from_key = 1
		current_consecutive = 1 

		# check descending consecutive integers 
		while hashmap.get(key - distance_from_key, False):
			del hashmap[key - distance_from_key] 
			current_consecutive += 1
			distance_from_key += 1

		distance_from_key = 1
		# check ascending consecutive integers 
		while(hashmap.get(key + distance_from_key)):
			del hashmap[key + distance_from_key]
			current_consecutive += 1
			distance_from_key += 1

		if current_consecutive > longest_consecutive:
			longest_consecutive = current_consecutive

		del hashmap[key]
	return longest_consecutive 

def main(array):
	print(f'Longest consecutive sequence in: {array}')
	print(f'has length of {get_longest_consecutive_sequence(array)}')

if __name__ == "__main__":
        # example usage:
	# $python longest_sequence.py 0,5,2,1,3,6,7 
	# -> Longest consecutive sequence in: [0, 5, 2, 1, 3, 6, 7]
	# -> has length of 4
	# argv[1] is a list of numbers separated by commas with no spaces 
	main([int(x) for x in sys.argv[1].split(',')])

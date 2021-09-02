# Answer to exercise 3 in chapter 13 
#
# Exercise from: A Common-Sense Guide to Data Structures and Algorithms 
# Level Up Your Core Programming Skills 
# by Jay Wengrow and edited by Brian MacDonald

import sys

def insertion_sort_find_greatest(array: list):
	"""sort in O(N^2) and return the greatest value"""
	newArray = array.copy()
	for index in range(1, len(newArray)): 
		j = index
		while j > 0 and newArray[j] < newArray[j-1]:
			newArray[j], newArray[j-1] = newArray[j-1], newArray[j] 
			j -= 1
	return newArray[-1]

def default_sort_find_greatest(array: list):
	"""Timsort is an O(nlogn) sort, return the greatest value"""
	temporarySorted = sorted(array) 
	return temporarySorted[-1]

def linear_search(array: list):
	"""Find and return the greatest value with a linear search"""
	maxValue = array[0]
	for number in array[1:]:
		if number > maxValue:
			maxValue = number
	return maxValue

def main(array: list):
	"""find the greatest value in array with various time complexities"""
	print('Greatest value using O(N^2) insertion sort:',
	      insertion_sort_find_greatest(array))
	print('Greatest value using default O(nlogn) Timsort:',
	      default_sort_find_greatest(array))
	print('Greatest value using a linear search O(N):', 
	      linear_search(array))

if __name__ == '__main__':
	# example usage:
        # $python find_greatest.py 5,2,3,7
        # -> Greatest value using O(N^2) insertion sort: 7
	# -> Greatest value using O(nlogn) Timsort: 7
	# -> Greatest value using a linear search O(N): 7
        # argv[1] is a list of numbers separated by commas with no spaces
	main([int(x) for x in sys.argv[1].split(',')])

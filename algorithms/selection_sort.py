import copy
import sys

def selection_sort(arr):
	"""selection sort the array"""
	arr = [int(x) for x in arr.split(',')]
	replica = copy.copy(arr)
	for i in range(len(arr)-1): 
		least_index = i 
		for j in range(i+1, len(arr)): 
			if arr[j] < arr[least_index]: 
				least_index = j 
		if least_index != i: 
			arr[i], arr[least_index] = arr[least_index], arr[i]
	print(f'original: {replica}')
	print(f'selection sort: {arr}')
	print(f'sorted: {sorted(replica)}')

if __name__ == "__main__":
	selection_sort(sys.argv[1])

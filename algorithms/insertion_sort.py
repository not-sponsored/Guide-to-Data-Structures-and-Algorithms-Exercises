import copy
import sys

def ins_sort(arr):
	"""insertion search the list:arr"""
	arr = [int(x) for x in arr.split(',')]
	replica = copy.copy(arr)
	for i in range(1, len(arr)):
		temp = arr[i]
		position = i - 1
		while position >= 0:
			if arr[position] > temp:
				arr[position + 1] = arr[position]
				position -= 1 
			else:
				break
		arr[position + 1] = temp
	print(f'orig: {replica}')
	print(f'insertion sort: {arr}')
	print(f'sorted: {sorted(replica)}')

if __name__ == "__main__":
	ins_sort(sys.argv[1])

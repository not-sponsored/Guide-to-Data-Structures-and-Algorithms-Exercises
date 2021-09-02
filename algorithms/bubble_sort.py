import sys

def bubble_sort(arr):
	"""bubble sort list:arr"""
	unsorted_index = len(arr) - 1
	is_sorted = False

	while not is_sorted:
		is_sorted = True
		for i in range(0, unsorted_index):
			if arr[i] > arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]
				is_sorted = False
				unsorted_index -= 1
	return arr

def main(arr):
	arr = [int(x) for x in arr.split(',')]
	print(f'Default sort: {sorted(arr)}')
	print(f'Bubble sort: {bubble_sort(arr)}')

if __name__ == '__main__':
	if len(sys.argv) > 1:
		main(sys.argv[1])

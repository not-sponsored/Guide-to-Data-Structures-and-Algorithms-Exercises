import sys

class SortableArray():
	def __init__(self, arr):
		self.arr = arr

	def partition(self, left, right):
		# choose right most as pivot
		pivot_index = right
		# get pivot value for compares
		pivot = self.arr[pivot_index]

		right -= 1
		print(f'left orig: {left} right orig: {right}')

		while True:
			# move left pointer until we hit a value >= pivot
			while self.arr[left] < pivot:
				print(f'left: {left}')
				left += 1
			print('left', left)

			# move right until hit a value <= pivot or hits 0 index
			while right > 0 and self.arr[right] > pivot:
				print(f'right: {right}')
				right -= 1
			print('right', right)
			
			# if left >= right then we break and swap
			if left >= right:
				break
			# if not we swap right and left and continue		
			else:
				self.arr[left], self.arr[right] = self.arr[right], self.arr[left]
				left += 1	
		# finally swap left and pivot
		self.arr[left], self.arr[pivot_index] = self.arr[pivot_index], self.arr[left]
		print(self.arr)
		return left
	
	def quicksort(self, left, right):
		# base case one element		
		if right - left <= 0:
			return
		# partition and get pivot
		pivot_index = self.partition(left, right)
		
		# recursively call for left partition
		self.quicksort(left, pivot_index - 1)

		# recursively call for right partition
		self.quicksort(pivot_index + 1, right)			 
			
	def quickselect(self, kth_lowest_num, left, right):
		# base case one element		
		if right - left <= 0:
			return self.arr[left]
		# partition and get pivot
		pivot_index = self.partition(left, right)
		
		# if kth is less than pivot, recursively call for left 
		if kth_lowest_num < pivot_index:
			self.quickselect(kth_lowest_num, left, pivot_index - 1)

		# if kth is greater than pivot, recursively call for right 
		elif kth_lowest_num > pivot_index:
			self.quickselect(kth_lowest_num, pivot_index + 1, right)			 
		# else we have the kth num bc kth = pivot_index
		else:
			# weird error returns a None
			print(f'kth {kth_lowest_num}: {self.arr[pivot_index]}')
			return self.arr[pivot_index] 

			
def main(arr, kth):
	sortable = SortableArray(arr)
	print(sortable.quickselect(kth, 0, len(arr) - 1))
	sortable.quicksort(0, len(arr) - 1)
	print(f'final sorted array: {sortable.arr}')

if __name__ == '__main__':
	main([int(x) for x in sys.argv[1].split(',')], int(sys.argv[2]))

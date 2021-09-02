import sys

class heap():
	def __init__(self, arr=None):
		self.array = [] 
		self.insert_many(arr)
	
	def insert_many(self, arr):
		if arr:
			for val in arr:
				self.insert(val)

	def insert(self, val: int):	
		self.array.append(val)
		self.heapify_up(len(self.array) - 1)

	def heapify_up(self, position):
		parent_index = self.get_parent_index(position)
		while self.array[parent_index] < self.array[position]:  
			self.swap(position, parent_index)
			position = parent_index
			parent_index = self.get_parent_index(position)

	def swap(self, position_one, position_two):
		self.array[position_one], self.array[position_two] = self.array[position_two], self.array[position_one]

	def get_parent_index(self, position):
		return max(0, (position - 1) // 2)

	def get_largest(self):
		largest = self.array.pop(0)
		self.reheap()
		return largest

	def reheap(self):
		position = 0
		last_item = self.array.pop()
		self.array.insert(position, last_item)
		while child_index := self.get_larger_child_index(position):
			self.swap(position, child_index)
			position = child_index

	def get_larger_child_index(self, position):
		largest_value_index = position
		left_child_index = (2*position) + 1
		right_child_index = (2*position) + 2 
		try:
			if self.array[left_child_index] > self.array[largest_value_index]:
				largest_value_index = left_child_index
		except:
			pass
		try:
			if self.array[right_child_index] > self.array[largest_value_index]:
				largest_value_index = right_child_index 
		except:
			pass
		if largest_value_index == position: 
			return None
		return largest_value_index

	def __str__(self):
		return str(self.array)

def main(arr):
	priority_queue = heap()
	priority_queue.insert_many(arr)
	print(priority_queue)
	print(f'get largest value from heap: {priority_queue.get_largest()}')
	print(priority_queue)

if __name__ == '__main__':
	main([int(x) for x in sys.argv[1].split(',')])


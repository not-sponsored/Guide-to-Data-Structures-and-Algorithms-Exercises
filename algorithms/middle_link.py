import sys

class Node():
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

	def print_node(self):
		print(self.value)

class SinglyLinkedList():
	def __init__(self, head=None):
		self.head = head

	def add_node(self, val):
		new_node = Node(val)
		if self.head == None:
			self.head = new_node 
		else:
			pointer = self.head
			while pointer.next != None:
				pointer = pointer.next
			pointer.next = new_node

	def add_many_nodes(self, values):
		for val in values:
			self.add_node(val)

	def print_nodes(self):
		pointer = self.head
		if pointer != None:
			pointer.print_node()
		while pointer.next != None:
			pointer = pointer.next
			pointer.print_node()

	def get_last_node(self):
		pointer = self.head
		if pointer == None:
			print('Error no nodes')
			return
		while pointer.next != None:
			pointer = pointer.next
		return pointer			

	def reverse_nodes(self):
		pointer_one = self.head
		# if no nodes do nothing		
		if pointer_one != None:
			pointer_two = pointer_one.next 
			pointer_one.next = None	
			# if only one node then we are done
			if pointer_two != None:
				# have pointers at nOne, nTwo, nThree
				pointer_three = pointer_two.next
				while pointer_three != None:
					# point second.next to first
					pointer_two.next = pointer_one
					# point first to second
					pointer_one = pointer_two
					# point second to third
					pointer_two = pointer_three
					# point third to fourth
					pointer_three = pointer_two.next
				# handle two nodes or more case
				pointer_two.next = pointer_one
				self.head = pointer_two	

	def count(self, pointer):
		if pointer == None:
			return 0
		if pointer.next == None:
			return 1
		else:
			return 1 + self.count(pointer.next) 

	def middle(self, node_cnt):
		middle = int(node_cnt/2)
		if middle == 0:
			print('Cannot divide list')
			return
		pointer = self.head
		count = 0	
		while count < middle:
			pointer = pointer.next
			count += 1
		return pointer


def main(arr):
	single_ll = SinglyLinkedList()
	single_ll.add_many_nodes(arr)
	node_count = single_ll.count(single_ll.head) 
	print(f"node count: {node_count}")	
	middle_node = single_ll.middle(node_count)
	print(f'middle node: {middle_node.value}')	
	# copy value of next node then link to next next node
	middle_node.value = middle_node.next.value
	middle_node.next = middle_node.next.next	
	single_ll.print_nodes()
if __name__ == '__main__':
	main([int(x) for x in sys.argv[1].split(',')])


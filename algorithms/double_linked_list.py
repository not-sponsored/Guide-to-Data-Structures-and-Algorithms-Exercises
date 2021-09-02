import sys

class Node():
	def __init__(self, value, prev=None ,next=None):
		self.value = value
		self.prev = prev
		self.next = next

	def print_node(self):
		print(self.value)

class DoublyLinkedList():
	def __init__(self, tail=None, head=None):
		self.head = head
		self.tail = tail

	def add_node(self, val):
		if self.head == None:
			new_node = Node(val)
			self.head = new_node
			self.tail = new_node 
		else:
			new_node = Node(val, self.tail)
			self.tail.next = new_node
			self.tail = new_node

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

	def reverse_print(self):
		pointer = self.tail
		if pointer != None:
			pointer.print_node()
		while pointer.prev != None:
			pointer = pointer.prev
			pointer.print_node()


def main(arr):
	double_ll = DoublyLinkedList()
	double_ll.add_many_nodes(arr)
	double_ll.print_nodes()
	print('reverse print')
	double_ll.reverse_print()

if __name__ == '__main__':
	main([int(x) for x in sys.argv[1].split(',')])


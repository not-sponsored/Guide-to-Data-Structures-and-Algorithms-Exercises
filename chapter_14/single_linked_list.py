# Answer to exercises 1, 3, 4 in chapter 14 
#
# Exercise/code from: A Common-Sense Guide to Data Structures and Algorithms 
# Level Up Your Core Programming Skills 
# by Jay Wengrow and edited by Brian MacDonald

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
		previous_node = None
		current_node = self.head
		next_node = self.head
		while current_node:
			next_node = next_node.next
			current_node.next = previous_node
			previous_node = current_node
			current_node = next_node
		self.head = previous_node	 


def main(array: list):
	single_ll = SinglyLinkedList()
	single_ll.add_many_nodes(array)
	print('---Display elements---')
	single_ll.print_nodes()

	print('---Display last element---')
	last_node = single_ll.get_last_node()
	last_node.print_node()

	print('\nReversing the linked list ...')
	single_ll.reverse_nodes()
	print('---Display the reversed list---')
	single_ll.print_nodes()

if __name__ == '__main__':
	# example usage:
        # $python single_linked_list.py 5,2,3,7
        # -> ---Display elements---
	# -> 5
	# -> 2
	# -> 3
	# -> 7
	# -> ---Display last element---
	# -> 7
	# ->
	# -> Reversing the linked list ...
	# -> ---Display the reversed list---
	# -> 7
	# -> 3
	# -> 2
	# -> 5 
        # argv[1] is a list of numbers separated by commas with no spaces
	main([int(x) for x in sys.argv[1].split(',')])

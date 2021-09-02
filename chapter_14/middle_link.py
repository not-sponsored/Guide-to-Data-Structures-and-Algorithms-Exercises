# Answer to exercise 5 in chapter 14 
#
# Exercise from: A Common-Sense Guide to Data Structures and Algorithms 
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


def main(array: list):
	single_ll = SinglyLinkedList()
	single_ll.add_many_nodes(array)
	print('---Before middle node removal---')
	single_ll.print_nodes()

	node_count = single_ll.count(single_ll.head) 
	print(f'Total node count: {node_count}')	

	middle_node = single_ll.middle(node_count)
	print(f'Middle node value: {middle_node.value}')	

	# copy value of next node then link to next next node
	middle_node.value = middle_node.next.value
	middle_node.next = middle_node.next.next	
	print('---After removal---')
	single_ll.print_nodes()

if __name__ == '__main__':
	# example usage:
        # $python middle_link.py 5,2,3
	# -> ---Before middle node removal---
	# -> 5
	# -> 2
	# -> 3
	# -> Total node count: 3
	# -> Middle node value: 2
	# -> ---After removal---
	# -> 5
	# -> 3
        # argv[1] is a list of numbers separated by commas with no spaces
	main([int(x) for x in sys.argv[1].split(',')])

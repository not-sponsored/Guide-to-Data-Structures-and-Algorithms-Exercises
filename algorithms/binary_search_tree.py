# Answer to exercise 3 in chapter 15 
# A large portion of the code is from the book 
#
# Exercise from: A Common-Sense Guide to Data Structures and Algorithms 
# Level Up Your Core Programming Skills 
# by Jay Wengrow and edited by Brian MacDonald

import sys

class TreeNode():
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


class Tree():
	def __init__(self, value=None):
		self.root = value

	def search(self, search_val, node):
		if node is None or node.value == search_val:
			return node
		elif search_val > node.value:
			return self.search(search_val, node.right)
		elif search_val < node.value:
			return self.search(search_val, node.left)
		
	def insert(self, node):
		if self.root is None:
			self.root = node
			return
		pointer = self.root
		while pointer:
			pointer_two = pointer
			if pointer.value < node.value:
				pointer = pointer.right
			elif pointer.value > node.value:
				pointer = pointer.left
		if pointer_two.value > node.value:
			print(f'insert left: {pointer_two.value, node.value}')
			pointer_two.left = node
		elif pointer_two.value < node.value:
			print(f'insert right: {pointer_two.value, node.value}')
			pointer_two.right = node

	def insert_nodes(self, values):
		for val in values:
			new_node = TreeNode(val)
			self.insert(new_node)

	def print_nodes(self, node):
		if node.left is not None:
			self.print_nodes(node.left)
		print(node.value)	
		if node.right is not None:
			self.print_nodes(node.right)

	def print_nodes_reverse(self, node):
		if node.right is not None:
			self.print_nodes_reverse(node.right)
		print(node.value)	
		if node.left is not None:
			self.print_nodes_reverse(node.left)
	
	def delete_val(self, deleteVal, node):
		self.root = self.delete(deleteVal, node)

	def delete(self, deleteVal, node):
		# base check if value does not exist
		if node is None:
			return None

		# find the node with the value
		if deleteVal > node.value:
			# return right subtree of values
			node.right = self.delete(deleteVal, node.right)
			return node
		if deleteVal < node.value:
			# return right subtree of values
			node.left = self.delete(deleteVal, node.left)
			return node
		if deleteVal == node.value:
			# case one with no children
			# base check would take care of but make explicit
			if node.left is None and node.right is None:
				return None

			# case two with one child (or tree)
			# return the right child for the subtree
			elif node.left is None:
				return node.right
			# return left child for the subtree
			elif node.right is None:
				return node.left
			
			# case three with both sides
			# need the least greatest node from this parent
			else:
				node.right = self.least_greatest(node.right,
								 node)
				return node

	def least_greatest(self, node, nodeToRemove):
		# already on right of node to delete so keep left for least
		if node.left is not None:
			node.left = self.least_greatest(node.left, nodeToRemove)
			return node
		# no left means current is successor and take its value 	
		else:
			nodeToRemove.value = node.value
			# return succesor's right to use as left
			return node.right

	def max_value(self):
		if self.root is None:
			return 
		pointer = self.root
		while pointer:
			pointer_two = pointer
			pointer = pointer.right
		return pointer_two.value 


def main(array: list, search_val: int, delete_val: int):
	bst = Tree()
	bst.insert_nodes(array)
	print('---Forward print---')
	bst.print_nodes(bst.root) 
	print('---Reverse print---')
	bst.print_nodes_reverse(bst.root) 

	print(f'\nSearching for: {search_val}')
	node_return = bst.search(search_val, bst.root)
	if node_return:
		print(f'Found: {node_return.value}')

	print(f'\nDeleting value: {delete_val}')
	bst.delete(delete_val, bst.root)	
	print('---Tree after delete---')
	bst.print_nodes(bst.root)

	print(f'Max value in tree: {bst.max_value()}')

if __name__ == '__main__':
	# example usage:
        # $python binary_search_tree.py 5,2,3,7 3 2
        # ->
        # argv[1] is a list of numbers separated by commas with no spaces
	# argv[2] is an int to search for in the binary tree
	# argv[3] is an int to delete from the binary tree
	main([int(x) for x in sys.argv[1].split(',')], int(sys.argv[2]),
	     int(sys.argv[3]))

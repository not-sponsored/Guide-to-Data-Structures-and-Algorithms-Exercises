import sys
import time

class TrieNode:
	
	def __init__(self):
		self.children = {}

class Trie:

	def __init__(self, arr=[]):
		self.root = TrieNode()
		if arr:
			self.insert_many(arr)

	def insert_many(self, arr):
		for word in arr:
			self.insert(word)

	def search(self, word):
		current_node = self.root
	
		for char in word:
			# has child with current character
			if current_node.children.get(char):
				# follow the child node
				current_node = current_node.children[char]
			else:
				# if char not in children then word not in trie
				return None
		return current_node

	def insert(self, word):
		current_node = self.root
		
		for char in word:
			# current node has child with char
			if current_node.children.get(char):
				# follow the child node
				current_node = current_node.children[char]
			else:
				# must be a new char so make a new node
				new_node = TrieNode()
				current_node.children[char] = new_node
				
				# follow newly created node
				current_node = current_node.children[char] 
		
		# add * to cap off the fully inserted word
		current_node.children['*'] = None

	def collect_all_words(self, node=None, word='', all_words=[]):
		# node is were we are collecting words from
		# word starts empty but grows as we add chars
		# all_words collects all the completed word strings together
		
		# current is passed node or defaults to root node
		current_node = node or self.root

		# iterate through current node's children
		for key, child_node in current_node.children.items():
			# if key is * we have a complete word for all_words
			if key == '*':
				all_words.append(word)
		
			# still in the middle of a word
			else: 
				# recursively get all words
				self.collect_all_words(child_node, word + key,
						       all_words)
						       

		return all_words

	def autocomplete(self, prefix):
		current_node = self.search(prefix)  # node at end or None
		if not current_node:
			return None                 # prefix not found in trie
		return self.collect_all_words(current_node) 


def main(arr, prefix):
	trie_object = Trie(arr)
	print(f'Autocomplete suggestions for prefix {prefix}: ', end='')
	print(trie_object.autocomplete(prefix))	

if __name__ == '__main__':
	main([str(x) for x in sys.argv[1].split(',')], str(sys.argv[2]))


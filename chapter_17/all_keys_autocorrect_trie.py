# Modified trie from the code presented in chapter 17 for exercises 3 and 4 
#
# Exercise/code from: A Common-Sense Guide to Data Structures and Algorithms 
# Level Up Your Core Programming Skills 
# by Jay Wengrow and edited by Brian MacDonald

import sys

class TrieNode:
	
	def __init__(self):
		self.children = {}


class Trie:

	def __init__(self, array=[]):
		self.root = TrieNode()
		if array:
			self.insert_many(array)

	def insert_many(self, array):
		for word in array:
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
		return self.collect_all_words(current_node, '', []) 

	def print_all_chars(self, node=None):
		current_node = node or self.root
		
		for key, child_node in current_node.children.items():
			print(key)
			if child_node:
				self.print_all_chars(child_node)

	def get_longest_prefix(self, word):
		longest_prefix = ''
		node = self.root

		for char in word:
			if char in node.children:
				longest_prefix += char
				node = node.children[char]
			else:
				break

		return longest_prefix

	def autocorrect(self, word):
		longest_prefix = self.get_longest_prefix(word)
		autocomplete_suggestions = self.autocomplete(longest_prefix)

		# get minimum difference word in terms of length and prefix
		differing_substr = word[len(longest_prefix):]
		len_of_differing = len(differing_substr)
		correct_suggestion = autocomplete_suggestions[0]
		minimum = abs(len_of_differing - len(correct_suggestion))

		for suggestion in autocomplete_suggestions[1:]:
			if abs(len_of_differing - len(suggestion)) < minimum:
				minimum = abs(len_of_differing
					      - len(suggestion))
				correct_suggestion = suggestion
			
		return longest_prefix + correct_suggestion 
				

def main(array: list, prefix: str, incorrect: str):
	trie_object = Trie(array)
	print(f'Autocomplete suggestions for prefix {prefix}: ', end='')
	print(trie_object.autocomplete(prefix))	
	print('---All keys in trie---')
	trie_object.print_all_chars()
	print(f'Autocorrect suggestion for {incorrect}: ', end='')
	print(trie_object.autocorrect(incorrect))

if __name__ == '__main__':
	# example usage:
        # $python all_keys_autocorrect_trie.py anchor,anchovy,bat,bare anch bac
	# -> Autocomplete suggestions for prefix anch: ['or', 'ovy']
	# -> --All keys in trie---
	# -> a 
	# -> n
	# -> c 
	# -> h
	# -> o
	# -> r
	# -> *
	# -> v
	# -> y
	# -> *
	# -> b
	# -> a
	# -> t
	# -> *
	# -> r
	# -> e
	# -> *
	# -> Autocorrect suggestion for bac: bat
	main([str(x) for x in sys.argv[1].split(',')], str(sys.argv[2]),
	     str(sys.argv[3]))

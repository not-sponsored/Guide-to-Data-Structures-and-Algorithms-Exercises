# Modified graph from chapter 18 
#
# Code from: A Common-Sense Guide to Data Structures and Algorithms 
# Level Up Your Core Programming Skills 
# by Jay Wengrow and edited by Brian MacDonald

import sys
from collections import deque 

class Vertex:
	
	def __init__(self, value: str):
		self.value = value
		self.adjacent = [] 

	def add_multiple_adjacent(self, vertices):
		for vertex in vertices:
			self.add_adjacent(vertex)

	def add_adjacent(self, vertex):
		if vertex in self.adjacent:
			return
		self.adjacent.append(vertex)
		vertex.add_adjacent(self)     # make graph bidirectional

	def dfs_traverse(self, vertex=None, visited_vertices={}):
		# is no passed vertex then default to self 
		vertex = vertex or self 

		# mark vertex as visited by adding it to the hash table
		visited_vertices[vertex.value] = True

		# show the vertex
		print(vertex.value)

		# iterate through current's vertices
		for adjacent_vertex in vertex.adjacent:
			if adjacent_vertex.value not in visited_vertices:
				self.dfs_traverse(adjacent_vertex,
						  visited_vertices)

	def dfs(self, search_value, vertex=None, visited_vertices={}):
		# if no passed vertex default to self
		vertex = vertex or self

		if vertex.value == search_value:
			return vertex

		visited_vertices[vertex.value] = True

		for adjacent_vertex in vertex.adjacent:
			if adjacent_vertex.value not in visited_vertices:
				if adjacent_vertex.value == search_value:
					return adjacent_vertex
				
				target_vertex = self.dfs(search_value,
						    	 adjacent_vertex,
						    	 visited_vertices)
				if target_vertex:
					return target_vertex
		return None 

	def bfs_traverse(self, starting_vertex=None):
		# use self if no starting given
		starting_vertex = starting_vertex or self

		visited_vertices = {}
		visited_vertices[starting_vertex.value] = True
		
		queue = deque([])
		queue.append(starting_vertex)

		while queue:
			# remove first vertex and set as current
			current_vertex = queue.popleft()

			print(current_vertex.value)
			
			# iterate over current's adjacent vertices
			for adjacent in current_vertex.adjacent:
				
				if adjacent.value not in visited_vertices:
					# mark as visited
					visited_vertices[adjacent.value] = True
				
					# add adjacent vertex to queue
					queue.append(adjacent)	


def main():
	alice = Vertex('Alice')
	bob = Vertex('Bob')
	candy = Vertex('Candy')
	derek = Vertex('Derek')
	elaine = Vertex('Elaine')
	fred = Vertex('Fred')
	gina = Vertex('Gina')
	helen = Vertex('Helen')
	irena = Vertex('Irena')

	# setup graph
	alice.add_multiple_adjacent([bob, candy, derek, elaine])
	bob.add_adjacent(fred)
	fred.add_adjacent(helen)
	candy.add_adjacent(helen)
	derek.add_multiple_adjacent([elaine, gina])
	gina.add_adjacent(irena)

	print('---DFS Traverse---')
	alice.dfs_traverse()
	print('---DFS Search---')
	dfs_search_result = alice.dfs('Helen')
	if dfs_search_result:
		print(dfs_search_result.value)

	print('---BFS Traverse---')
	alice.bfs_traverse()

if __name__ == '__main__':
	main()


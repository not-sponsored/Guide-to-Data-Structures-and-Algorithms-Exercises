# Answer to exercise 4 and 5 of chapter 18
# Modified graph from chapter 18 
#
# Exercise/code from: A Common-Sense Guide to Data Structures and Algorithms 
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

	def bfs(self, search_value: str, starting_vertex=None):
		# use self if no starting given
		starting_vertex = starting_vertex or self

		visited_vertices = {}
		visited_vertices[starting_vertex.value] = True
		
		queue = deque([])
		queue.append(starting_vertex)

		while queue:
			# remove first vertex and set as current
			current_vertex = queue.popleft()

			# return the vertex if the search matches
			if current_vertex.value == search_value:
				return current_vertex
			
			# iterate over current_vertex's adjacent vertices
			for adjacent in current_vertex.adjacent:
				if adjacent.value not in visited_vertices:
					# mark as visited
					visited_vertices[adjacent.value] = True
				
					# add adjacent vertex to queue
					queue.append(adjacent)	

		return None

	def unweighted_shortest_path(self, search_value='', starting=None):
		starting = starting or self

		visited_vertices = {}
		visited_vertices[starting.value] = True
		shortest = {}

		queue = deque([])
		queue.append(starting)

		run_outer_loop = True 
		while queue and run_outer_loop:
			current = queue.popleft()

			for adjacent in current.adjacent:
				if adjacent.value not in visited_vertices:
					shortest[adjacent.value] = current
					if adjacent.value == search_value:
						run_outer_loop = False
						break
					visited_vertices[adjacent.value] = True
					queue.append(adjacent)
		if not run_outer_loop:
			path = [search_value]
			while vertex:=shortest.get(search_value, 0):
				path.insert(0, vertex.value)
				search_value = vertex.value
			return path

		return None


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

	print('---DFS Traverse Starting From Alice---')
	alice.dfs_traverse()
	
	dfs_name = input('Enter name to depth first search for: ')
	print('---DFS Search---')
	dfs_search_result = alice.dfs(dfs_name)
	if dfs_search_result:
		print(dfs_search_result.value)

	print('---BFS Traverse---')
	alice.bfs_traverse()

	bfs_name = input('Enter name to breadth first search for: ')
	print('---BFS Search---')
	bfs_search_result = alice.bfs(bfs_name)
	if bfs_search_result:
		print(bfs_search_result.value)

	# second graph setup
	idris = Vertex('Idris')
	kamil = Vertex('Kamil')
	lina = Vertex('Lina')
	sasha = Vertex('Sasha')
	marco = Vertex('Marco')
	ken = Vertex('Ken')
	talia = Vertex('Talia')
	name_map = {'Idris': idris, 'Kamil': kamil, 'Lina': lina,
		    'Sasha': sasha, 'Marco': marco, 'Ken': ken, 'Talia': talia} 

	idris.add_multiple_adjacent([kamil, talia])
	kamil.add_adjacent(lina)
	lina.add_adjacent(sasha)
	sasha.add_adjacent(marco)
	marco.add_adjacent(ken)
	ken.add_adjacent(talia)	

	print('\n---New Graph for Shortest Unweighted Path Test---')
	print('---DFS Traversal---')
	idris.dfs_traverse()

	print('---Path Search---')
	starting_name = input('Enter valid name to start path search at: ')
	ending_name = input('Enter name to end search at: ')
	if vertex:=name_map.get(starting_name, None):
		print(f'---Shortest Path {starting_name} to {ending_name}---')
		print(vertex.unweighted_shortest_path(ending_name))

if __name__ == '__main__':
	# example usage:
        # $python bfs_shorest_path_traversal.py
	# Output omitted due to length and required user input ... 
	main()

def detecting_cyclicgraph(g):
	"""Return True if the directed graph g has a cycle.
	g must be represented as a dictionary mapping vertices to
	iterables of neighbouring vertices. 
	"""
	path = set()
	visited = set()

	def visit(vertex):
		if vertex in visited:
			return False
		visited.add(vertex)
		path.add(vertex)
		for neighbour in g.get(vertex, ()):
			if neighbour in path or visit(neighbour):
				return True
		path.remove(vertex)
		return False

	return any(visit(v) for v in g)

# Dinic's Algorithm

# while searching about max flow algorithms, came across Edmons-karp algorihtm with O(V E^2) and
# Dinic's Algorithm with O(V^2 E) which was actually a development compared to Edmons-karp algorithm and also came out in
# 1970 which is leatest compared to 1969. There were few more algorithms came later like tarjan, Goldberg,
# Goldberg and Targaj. But while surfing various sites, Dinic's algorithm was the most praised one, so choosed to go with it. 


class Edge:
	def __init__(self, v, flow, C, rev):
		self.v = v
		self.flow = flow
		self.C = C
		self.rev = rev

# Residual Graph
class Graph:
	def __init__(self, V):
		self.adj = [[] for i in range(V)]
		self.V = V
		self.level = [0 for i in range(V)]

	# add edge to the graph
	def addEdge(self, u, v, C):

		# Forward edge : 0 flow and C capacity
		a = Edge(v, 0, C, len(self.adj[v]))

		# Back edge : 0 flow and 0 capacity
		b = Edge(u, 0, 0, len(self.adj[u]))
		self.adj[u].append(a)
		self.adj[v].append(b)

	# Finds if more flow can be sent from s to t
	# Also assigns levels to nodes
	def BFS(self, s, t):
		for i in range(self.V):
			self.level[i] = -1

		# Level of source vertex
		self.level[s] = 0

		# Create a queue, enqueue source vertex
		# and mark source vertex as visited here
		# level[] array works as visited array also
		q = []
		q.append(s)
		while q:
			u = q.pop(0)
			for i in range(len(self.adj[u])):
				e = self.adj[u][i]
				if self.level[e.v] < 0 and e.flow < e.C:

					# Level of current vertex is
					# level of parent + 1
					self.level[e.v] = self.level[u]+1
					q.append(e.v)

		# If we can not reach to the sink we
		# return False else True
		return False if self.level[t] < 0 else True

# A DFS based function to send flow after BFS has
# figured out that there is a possible flow and constructed levels
	def sendFlow(self, u, flow, t, start):
		# Sink reached
		if u == t:
			return flow

		# Traverse all adjacent edges one -by -one
		while start[u] < len(self.adj[u]):

			# Pick next edge from adjacency list of u
			e = self.adj[u][start[u]]
			if self.level[e.v] == self.level[u]+1 and e.flow < e.C:

				# find minimum flow from u to t
				curr_flow = min(flow, e.C-e.flow)
				temp_flow = self.sendFlow(e.v, curr_flow, t, start)

				# flow is greater than zero
				if temp_flow and temp_flow > 0:

					# add flow to current edge
					e.flow += temp_flow

					# subtract flow from reverse edge
					# of current edge
					self.adj[e.v][e.rev].flow -= temp_flow
					return temp_flow
			start[u] += 1

	# Returns maximum flow in graph
	def DinicMaxflow(self, s, t):

		# Corner case
		if s == t:
			return -1

		# Initialize result
		total = 0

		# Augument the flow while there is path
		# from source to sink
		while self.BFS(s, t) == True:

			# store how many edges are visited
			# from V { 0 to V }
			start = [0 for i in range(self.V+1)]
			while True:
				flow = self.sendFlow(s, float('inf'), t, start)
				if not flow:
					break

				# Add path flow to overall flow
				total += flow

		# return maximum flow
		return total



def solution(entrances, exits, path):
    # Your code here
    total_possible_nodes = len(path) * len(path[0])
    g = Graph(total_possible_nodes + 3)

    for i in range(len(path)):
        for j in range(len(path[i]) - 1, -1, -1):
            if path[i][j] > 0:
                g.addEdge(i, j, path[i][j])
        # after every iteration trying to save even tiny space to free up more memory  
        path[i] = []
    # as we have graph now, the path array of array can be deleted to free up space 
    del path

    # to solve multiple start, came up with mine-own solution to 
    # add a start node and connect it with all enterances noded with max flow range and consider this one as start node.
    start_node = total_possible_nodes + 1
    max_bunney = 2000000

    for i in entrances:
        g.addEdge(start_node, i, max_bunney)

    # same trick as start node to handle multiple exit nodes or sinks , added one end node and connected with sinks with max
    # flow range and considered it as new sink
    end_node = total_possible_nodes + 2
    for i in exits:
        g.addEdge(i, end_node, max_bunney)

    # total runtime complexity is O(V^2 E) : V == number of vertices and E == number of edges
    return g.DinicMaxflow(start_node, end_node)




print(solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]))


print(solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))

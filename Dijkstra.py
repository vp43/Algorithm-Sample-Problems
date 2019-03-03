
class Graph(object):
   
    def __init__(self, node, dist = 1000000000000):
        self.node = node
        self.distance = dist

def heapify(nodes, i, heapsize):

    left = 2 * i + 1
    right = 2 * i + 2
    smallest = i

    if (left < heapsize) and (nodes[left].distance < nodes[i].distance ):
        smallest = left
    if (right < heapsize) and (nodes[right].distance < nodes[i].distance):
        smallest = right
    if smallest != i:
        temp = nodes[smallest]
        nodes[smallest] = nodes[i]
        nodes[i] = temp
        heapify(nodes, smallest, heapsize)

def Buildminheap(nodes):

    heapsize = len(nodes)
    for i in range(int(len(nodes)/2), -1, -1):
        heapify(nodes, i, heapsize)
    return nodes

def shortestPaths( nodeList ):

	neighbours = {}
	for edge in nodeList :
		u = edge[0]
		v = edge[1]
		distance = edge[2]
		if u in neighbours:
			neighbours[u].append([v,distance])
		else:
			neighbours[u] = [[v,distance]]
		if v in neighbours:
			neighbours[v].append([u,distance])
		else:
			neighbours[v] = [[u,distance]]
	nList = []
	for node in neighbours:
		nList.append(Graph(node))
	nList[0].distance = 0
	prev = {}
	prev[0] = 0
	final_distance = {}
	while (len(nList) > 0):
		current_node = nList[0]
		final_distance[current_node.node] = current_node.distance
		nList = nList[1:]
		for edges in neighbours[current_node.node]:
			adj_node = edges[0]
			distance = edges[1]
			for i in range(len(nList)):
				if nList[i].node == adj_node:
					if  nList[i].distance > current_node.distance + distance:
						nList[i].distance = current_node.distance + distance
						prev[nList[i].node] = current_node.node
						nList[:i+1] = Buildminheap(nList[:i+1])
	path = {}
	path[0] = [0]
	for node,previous in prev.items():
		if node == 0:
			path[node] = [0]
		else:
			path[node] = [previous, node]
		start = node
		while (previous > 0):
			start = previous
			previous = prev[start]
			path[node].insert(0, previous)
	rv = []

	for node, p in path.items():
		if final_distance[node] < 1000000000000:
			rv.append(((final_distance[node], p)))
	return rv




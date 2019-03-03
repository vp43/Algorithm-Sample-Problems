from collections import defaultdict

parent = dict()
rank = dict()

class Graph(object):
   
	def __init__(self, node, cost = 1000000000000):
		self.index = node
		self.cost = cost
		self.prev = self
		self.neighborList = []


def makeset(x):
	parent[x] = x
	rank[x] = 0


def find(x):
	if x != parent[x]:
		parent[x] = find(parent[x])
	return parent[x]


def union(x,y):
	rx = find(x)
	ry = find(y)
	if rx == ry:
		return
	if rank[rx] > rank[ry]:
		parent[ry] = rx
	else:
		parent[rx] = ry
		if rank[rx] == rank[ry]:
			rank[ry] = rank[ry] + 1	


def Maxheapify(A,i,heapsize):
	l = 2*i
	r = 2*i + 1
	if (l <= heapsize) and (A[l][2] > A[i][2]):
		largest = l
	else:
		largest = i
	if (r <= heapsize) and (A[r][2] > A[largest][2]):
		largest = r
	if largest != i:
		A[i],A[largest] = A[largest],A[i]
		Maxheapify(A,largest,heapsize)


def BUildMaxHeap(A,heapsize):
	for i in range(int(heapsize/2),-1,-1):
		Maxheapify(A,i,heapsize)

		
def HeapSort(A):
	heapsize = len(A)-1
	BUildMaxHeap(A,heapsize)
	for i in range(len(A)-1,0,-1):
		A[0],A[i] = A[i],A[0]
		heapsize = heapsize-1
		Maxheapify(A,0,heapsize)
	return A


def sortList(NewList):
	NewList = HeapSort(NewList)
	return NewList


def Primheapify(nodes, i, heapsize):
	l = 2 * i + 1
	r = 2 * i + 2
	smallest = i
	if (l < heapsize) and (nodes[l].cost < nodes[i].cost ):
		smallest = l
	if (r < heapsize) and (nodes[r].cost < nodes[i].cost):
		smallest = r
	if smallest != i:
		temp = nodes[smallest]
		nodes[smallest] = nodes[i]
		nodes[i] = temp
		Primheapify(nodes, smallest, heapsize)


def PrimBuildMinheap(nodes):
	heapsize = len(nodes)
	for i in range(int(len(nodes)/2), -1, -1):
		Primheapify(nodes, i, heapsize)
	return nodes


def MST_Kruskel(inputList):
	V = []
	NewList = []
	dist = 0 
	rv = ()
	for edge in inputList:
		flag = 0
		f = 0
		u = edge[0]
		for i in V:
			if i == u:
				flag = 1
		if flag == 0:
			V.append(u)

		v = edge[1]
		for i in V:
			if i == v:
				f = 1
		if f == 0:
			V.append(v)		
	for u in V:
		makeset(u)
	path = []
	NewList = sortList(inputList)
	for edge in NewList:
		tempList = []
		u = edge[0]
		v = edge[1]
		flag = 0
		f = 0
		if find(u) != find(v):
			tempList.append(u)
			tempList.append(v)
			dist = dist + edge[2]
			union(u,v)
			path.append(tuple((tempList)))
	rv = tuple([dist] + [path])	
	return rv
	
			
def MST_Prim(inputList):
	Vertices = {}
	nList = []
	path = []
	nodeList = {}
	FinalCost = 0

	for edge in inputList:
		cost = edge[2]
		if edge[0] in Vertices:
			u = Vertices[edge[0]]
		else:
			u = Graph(edge[0])
			Vertices[edge[0]] = u
			nList.append(u)

		if edge[1] in Vertices:
			v = Vertices[edge[1]]
		else:
			v = Graph(edge[1])
			Vertices[edge[1]] = v
			nList.append(v)
		u.neighborList.append([v, cost])
		v.neighborList.append([u,cost])
		nodeList[edge[0], edge[1]] = cost
		nodeList[edge[1], edge[0]] = cost
		
	nList[0].cost = 0

	while ( len(nList) > 0 ):
		current_node = nList[0]
		nList = nList[1:len(nList)]
		PrimBuildMinheap(nList)

		for adj_node in current_node.neighborList:
			if (adj_node[0] in nList) and (adj_node[0].cost > adj_node[1]):
				adj_node[0].cost = adj_node[1]
				adj_node[0].prev = current_node
				index = nList.index(adj_node[0])
				nList[:index+1] = PrimBuildMinheap(nList[:index+1])
				
	for x, node in Vertices.items():
		if x != node.prev.index:
			path.append([x, node.prev.index])
			FinalCost = FinalCost + nodeList[x, node.prev.index]

	rv = tuple([FinalCost] + [path])
	return rv
			
			



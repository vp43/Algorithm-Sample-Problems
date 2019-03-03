from collections import defaultdict

def BFS(source,sink):
	visited = {e: False for e in vertices}
	queue = []
	queue.append(source)
	visited[source] = True
	
	while queue:
		u = queue.pop(0)
		if u not in res_graph:
			graph[u] = {}
		for v in res_graph[u]:
			flow = res_graph[u][v]
			if visited[v] == False and flow > 0:
				queue.append(v)
				visited[v] = True
				parent[v] = u
	return True if visited[sink] else False

def res_path(source,sink, vertices, parent, min_flow):

	v = sink
	while v != source:
		u,w = parent[v]
		vertices[u][v] -= min_flow
		vertices[v][u] += min_flow
		v = u

def dij_path(source,sink,vertices):
	tempdict = {}
	d = defaultdict(lambda: 0)

	tempdict[source] = -1<<30
	d[source] = 1<<30
	visited = set()
	parent= defaultdict()

	while tempdict != []:
		try:
			u, flow = tempdict.popitem()
		except:
			return None
		visited.add(u)

		if u == sink:
			return parent

		for v, flow in vertices[u].items():
			if v not in visited and flow:
				if d[v]<min(d[u],flow):
					d[v] = min(d[u],flow)
					tempdict[v] = -d[v]
					parent[v] = (u,flow)


def Max_Flow_Short(source, sink, inputList):
	
	global res_graph
	global parent
	res_graph = {}
	graph = {}
	#max_flow = 0
	global vertices 
	vertices = []

	for u,v,cost in inputList:
		if u not in res_graph:
			res_graph[u] = {}
		if v not in res_graph:
			res_graph[v] = {}		
		res_graph[u][v] = cost
		res_graph[v][u] = 0

		if u not in graph:
			graph[u] = {}
		if v not in graph:
			graph[v] = {}		
		graph[u][v] = cost
		graph[v][u] = 0
		vertices.append(u)
		vertices.append(v)

	vertices = list(set(vertices))
    
	parent = {e:-1 for e in vertices}
	max_flow = 0

	while BFS(source,sink):
		path_flow = float("Inf")
		
		v = sink
		while v!= source:
			path_flow = min(path_flow,res_graph[parent[v]][v])
			v = parent[v]
		max_flow = max_flow + path_flow
		
		v = sink
		while (v!= source):
			u = parent[v]
			res_graph[u][v] = res_graph[u][v] - path_flow
			res_graph[v][u] = res_graph[v][u] + path_flow
			v = parent[v]
			
		path = []
		for u in res_graph:
				for v in res_graph[u]:
					final_flow = graph[u][v] - res_graph[u][v]
					if final_flow > 0:
						p = (u,v,final_flow)
						path.append(p)
	return (max_flow,path)
	
def Max_Flow_Fat(source, sink, G):
	vertices = defaultdict(lambda:defaultdict(lambda:0))

	for u,v,cost in G:
		vertices[u][v]=max(vertices[u][v],cost)
		vertices[v][u]=max(vertices[v][u],0)

	max_flow=0
	
	while 1:
		parent=dij_path(source, sink, vertices)

		if parent == None:	
			return (max_flow,[])

		min_flow = 1<<30
		v = sink
		while v != source:

			u,flow = parent[v]
			min_flow = min(min_flow,flow)
			v = u
		max_flow += min_flow
		res_path(source,sink,vertices,parent,min_flow)

	return None

					
#print(Max_Flow_Fat(0, 3, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))


def backtrack(b,i,j):
	p = ""
	while(i>0 and j>0):
		value = min(b[i-1][j-1],b[i-1][j],b[i][j-1])
		if (value == b[i-1][j-1]):
			if(value == b[i][j]):
				 p = "_" + p				
			else:
				 p = "R" + p
			i = i-1
			j = j-1
		elif (value == b[i-1][j]):
			p = "I" + p
			i = i-1
			j = j
		else:
			p = "D" + p
			i = i
			j = j-1
	while(i>0 and j==0):
		p = "I" + p
		i = i-1
	
	while(i==0 and j>0):
		p = "D" + p
		j = j-1	
	return p
		
		
	
def editDistance(str1,str2):

	m = len(str1) +1
	n = len(str2) +1
	d = [[0 for i in range(m)] for j in range(n)]
	bt = [[0 for i in range(m)] for j in range(n)]
	val = ""
	
	
	for i in range(0,n):
		d[i][0] = i
	for j in range(0,m):
		d[0][j] = j
	for i in range(1,n):
		for j in range(1,m):
			r = 1
			if(str1[j-1] == str2[i-1]):
				r = 0 
			d[i][j] = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1] + r)
			
	path = backtrack(d,i,j)
	return d[n-1][m-1],path
					
	
	



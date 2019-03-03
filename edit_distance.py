from collections import defaultdict

def compute_fkp(a,b,f,k,p,m,n):
	t = max(f[k][p-1]+1,f[k-1][p-1],f[k+1][p-1]+1)
	while (t+1<=m and t+1>=0 and t+1+k<=n and t+1+k>=0 and a[t+1] == b[t+1+k]):
		t = t + 1
	f[k][p] = t


def editDistance(a,b):
	if a == '' and b== '':
		return 0
	a = ' '+ a
	b = ' '+ b
	m = len(a)-1
	n = len(b)-1
	p = -1
	r = p-min(m,n)

	f = defaultdict(lambda: defaultdict (lambda: -1<<30))
	for i in range(m+1):
		for j in range(n+1):
			k=j-1
			if (k<0):
				f[k][abs(k)-1] = abs(k)-1
			else:
				f[k][abs(k)-1] = -1

	while f[n-m][p]!=m:
		p=p+1
		r=r+1
		if r<=0:
			for k in range(-p,p+1):
				compute_fkp(a,b,f,k,p,m,n)
		else:
			for k in range(max(-m,-p),min(n,p)+1):
				compute_fkp(a,b,f,k,p,m,n)
	s=p
	return s

		





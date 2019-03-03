#heapSort


def Maxheapify(A,i,heapsize):
	l = 2*i
	r = 2*i + 1
	if (l <= heapsize) and (A[l] > A[i]):
		largest = l
	else:
		largest = i
	if (r <= heapsize) and (A[r] > A[largest]):
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
	
A=[3,2,1,60,40,200,102,31,54,67]
m=[]
m=HeapSort(A)
print m
			




def CompleteSet(size1,size2):

    if size2 == 0:
        return [[]]
    else:
        rv = []
        for value in CompleteSet(size1,size2 - 1):
            for index in range(size1):
                rv.append([index]+value)
        return rv

def is_Safe(t,c,l):
	for pos in range(l):
		if c == t[pos]:
			return False
		if abs(l-pos) == abs(c-t[pos]):
			return False
	return True

def btrack(NQ,rv,t=[]):
	if NQ <= 0:
		return [[]]
	if NQ == len(t):
		rv.append(t)
		return
	for c in range(NQ):
        	if is_Safe(t,c,len(t)):
            		btrack(NQ,rv,t+[c])
def B_Queens(NQ):
	rv = []
	btrack(NQ,rv)
	return rv

def E_Queens(NQ):

	t = CompleteSet(NQ,NQ)
	rv = []
	if NQ <= 0:
		return [[]]
	for combination in t:
		f = 0
		for index in range(0,len(combination)):
			if combination[index] in combination[index+1:]:
				f = 1
		for i in range(0,len(combination) - 1,):
			for j in range(i+1, len(combination)):
				if (((combination[i]-i)==(combination[j]-j))or((combination[i]+i) == (combination[j]+j))):
					f = 1
		if f == 0:
			rv.append(combination)
	return rv




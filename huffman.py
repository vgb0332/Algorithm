def swap(A, a, b):
	#swap method
	A[a], A[b] = A[b], A[a]
	
def extract_min(H):
	#delete the min of min-heap H, heapify, and return the min
	#heapify() would be needed
	min = H[0]
	del H[0]
	
	k = len(H) - 1
	while (k//2 >= 0):
		if(H[k][1] < H[k//2][1]):
			swap(H, k, k//2)
			k = k//2
		else:
			break
	
	#print H
	#make_heap(H)
	return min
	
def insert(H, i, f):
	#insert a tupel(i,f) into heap H
	H.append((i,f))
	k = len(H) - 1
	while (k//2 >= 0):
		if(H[k][1] < H[k//2][1]):
			swap(H, k, k//2)
			k = k//2
		else:
			break
	
	#print H
	

def make_heap(H):
	n = len(H)
	for i in range(n/2, -1, -1):
		min_heapify(H, n, i)
		
def heapify(H, n, i):
	while (2*i+1) < n: 
		L = 2*i + 1
		R = 2*i + 2
		if (H[i] > H[L]) : 
			m = L
		else: m = i
		if (R > n) and (H[m] > H[R]): 
			m = R
		if i != m: 
			swap(H,i,m)
			i = m
		else: 
			break
	
def huffman(f):
	# f: a list of n frequencies + n additional elements (total 2n)
	# H: a min-heap of tuples(i, f[i])
	# L[i] = left child of i, R[i] = right child of i, P[i] = parent of inser
	n = len(f)
	L = [-1]*(2*n-1)
	R = [-1]*(2*n-1)
	P = [-1]*(2*n-1)
	H = []
	for i in range(n):
		insert(H, i, f[i]) #make a min-heap H with f[0],f[1], ..., f[n-1]
	
	for i in range(n, 2*n-1):
		x = extract_min(H)
		y = extract_min(H)
		f[i] = f[x][1] + f[y][1]
		print f[i]
		L[i] = x, R[i] = y, P[x] = P[y] = i
		insert(H, i, f[i])
		
	# compute binary codes and the cost with L, R, P
	return cost

	
	
f = [43, 12, 13, 7, 9, 16]
huffman(f)
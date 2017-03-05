def LIS(A):
	n = len(A)
	# Initialize List S, I
	S = [0] * n
	I = [0] * n
	S[0] = 1
	for i in range(n):
		I[i] = i
	
	# Using double for loop, calculate S[i], I[i] at the same time
	for i in range(1, n):
		S[i] = 1
		for j in range(i):
			if(A[i] > A[j] and S[i] <= S[j]):
				S[i] = S[j] + 1
				I[i] = j

	max = S[0]
	last_index_LIS = 0
	for i in range(1, n):
		if(max < S[i]): 
			max = S[i]
			last_index_LIS = i
	len_LIS = max
	#print len_LIS, last_index_LIS
	return len_LIS, last_index_LIS, I
		
	# Len of LIS = max(S[i]) over i = 0, ..., n-1
	# Index of A which last element of LIS is stored = i that becomes max(S[i])
	# return len of LIS, Index of A of last element of LIS, Index
		
A = raw_input().split()
for i in range(len(A)):
	A[i] = int(A[i])
len_LIS, last_index_LIS, I = LIS(A)

ANS = []
len_LIS, last_index_LIS, I = LIS(A)

print len_LIS
while len_LIS > 0:
	ANS.append(A[last_index_LIS])
	last_index_LIS = I[last_index_LIS]
	len_LIS -= 1
	
for i in range(len(ANS)-1, -1, -1):
	print ANS[i], 

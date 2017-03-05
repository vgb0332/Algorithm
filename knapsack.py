def knapsack_fractional(I, a, s):
	max_profit = 0
	current_size = s
	for i in range(a, len(I)):
		if(I[i][1] <= current_size):
			max_profit += I[i][0]
			current_size -= I[i][1]
		else:
			while(current_size > 0):
				max_profit += I[i][0]/I[i][1]
				current_size -= 1
	#print max_profit
	return max_profit
	
def knapsack(I, X, Y, a, s):
	print X
	global MaxProfit
	p_v = 0
	for i in range(a):
		if(X[i] == 1): 
			p_v+=I[i][0]
	if(a < 0): return
	'''		
	if(a >= len(I)): 
		MaxProfit = p_v
		print MaxProfit, X
		return
	'''
	for i in range(1,-1,-1):
		if(i == 1):
				X[a] = 1
				knapsack(I, X, Y, a+1, s-I[a][1])
		if(i == 0):
			if MaxProfit < p_v + knapsack_fractional(I, a+1, s):
				X[a] = 0
				#print p_v, knapsack_fractional(I, a+1, s), p_v+ knapsack_fractional(I, a+1, s) , X
				knapsack(I, X, Y, a+1, s)
	
	
# I : (profit, size) tuple list
# K : sack's size, P : Item's profits(in float), S : Item's sizes(in float)
# X : [0] * len(A) select(1) or not select(0)
# Y = [] maxProfit selection list
# MaxProfit = 0
# Decreasing Order of I

K = int(raw_input())
P = raw_input().split()
S = raw_input().split()
I = []

for i in range(len(P)):
	P[i] = float(P[i])
	S[i] = float(S[i])
	I.append((P[i], S[i]))

X = [0] * len(P)
Y = []	
MaxProfit = 0

I.sort(key=lambda tup: tup[0]/tup[1], reverse=True)

#print K
#print P
#print S
#print I


knapsack(I, X, Y, 0, K)
#print maxProfit

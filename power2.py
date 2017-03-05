#power.py
import time

def slow_power(a, n):
	if n == 0: return 1
	return a*slow_power(a, n-1)


def fast_power(a, n):
	if(n == 0): return 1;
	res = fast_power(a, n/2);
	if(n % 2 == 0): return res*res;
	else: return a*res*res;
	
a = 5
n = 10

while(n!= 100):
	start = time.clock()
	slow_power(a,n)
	mid = time.clock()
	fast_power(a, n)
	end = time.clock()
	print "%f, %f" %(mid-start, end-mid)
	n = n + 10
	
print
a = 10
n = 10

while(n!= 100):
	start = time.clock()
	slow_power(a,n)
	mid = time.clock()
	fast_power(a, n)
	end = time.clock()
	print "%f, %f" %(mid-start, end-mid)
	n = n + 10
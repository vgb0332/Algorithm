#power.py
import time

#def of slow_power & fast_power function
def slow_power(a, n):
	if n == 0: return 1
	return a*slow_power(a, n-1)
	
def fast_power(a, n):
	if(n == 0): return 1
	#res = fast_power(a, n/2)
	if(n % 2 == 0): return fast_power(a*a, n/2)
	else: return a*fast_power(a*a, (n-1)/2)
	
#acheive inputs a, n	
a = int(raw_input())
n = int(raw_input())

#calculate operation time
start = time.clock()
print slow_power(a,n)
mid = time.clock()
print fast_power(a, n)
end = time.clock()
print "%f, %f" %(mid-start, end-mid)
import time
from check_sort import check_sort

#This is for storing swap and comp variables for each sort
swapNcomp = [0]*2
def swap(A, a, b):
	#swap method
	A[a], A[b] = A[b], A[a]

def selection(A):
	# sel sort
	n = len(A)
	while n > 0:
		max = A[0]
		index = 0
		for i in range(1, n):
			if(max > A[i]): #compare++
				swapNcomp[1] = swapNcomp[1] + 1
				max = A[i]
				index = i
		swap(A, index, n-1) #swap++ 
		swapNcomp[0] = swapNcomp[0] + 1
		n = n - 1
	

def insertion(A):
	#insertion sort
	n = len(A)
	for i in range(1, n):
		pos = i
		while(A[pos] < A[pos - 1] and pos>=1):#compare+2
			swap(A, pos, pos-1)
			pos = pos - 1
			swapNcomp[0] = swapNcomp[0] + 1
			swapNcomp[1] = swapNcomp[1] + 2
		
def bubble(A):
	#bubble sort
	n = len(A)
	for i in range(n, 0 , -1):
		for j in range(0, n-1):	
			if(A[j] > A[j+1]): #comp++
				swap(A, j, j+1) #swap++
				swapNcomp[0] = swapNcomp[0] + 1
				swapNcomp[1] = swapNcomp[1] + 1
				
def quick(A):
	# quick_sort(A, first, last)
	quick_sort(A, 0, len(A)-1)
	
def quick_sort(A, first, last):
	if first >= last: #comp
		swapNcomp[1] = swapNcomp[1] + 1
		return
	
	p = A[first]
	left = first + 1
	right = last

	while left <= right:
		while left <= last and A[left] <= p: #compare++
			swapNcomp[1] = swapNcomp[1] + 1
			left = left + 1
		while right >= left and A[right] >= p: #compare++
			swapNcomp[1] = swapNcomp[1] + 1
			right = right - 1
		if left < right: #compare++
			swapNcomp[1] = swapNcomp[1] + 1
			swap(A, left, right) #swap++
			swapNcomp[0] = swapNcomp[0] + 1
		
	swap(A, first, right)#swap++
	swapNcomp[0] = swapNcomp[0] + 1
	quick_sort(A, first, right-1)
	quick_sort(A, left, last)
	
def merge(A):
	#merge_sort(A, first, last)
	merge_sort(A, 0, len(A)-1)

def merge_sort(A, first, last):
	if (len(A)<=1): #compare++ 
		swapNcomp[1] = swapNcomp[1]+1
		return 
	mid = len(A)//2
	
	left = A[:mid]
	right = A[mid:]
	
	merge_sort(left, first, mid)
	merge_sort(right, mid, last)
	
	i = 0
	j = 0
	k = 0
	while i< len(left) and j < len(right): #compare++
		swapNcomp[1] = swapNcomp[1]+1
		if(left[i] <= right[j]): #compare++
			swapNcomp[1] = swapNcomp[1]+1
			A[k] = left[i]
			i = i + 1
		else: #compare++
			swapNcomp[1] = swapNcomp[1]+1
			A[k] = right[j]
			j = j + 1
		k = k + 1
	
	while i < len(left): #compare++
		swapNcomp[1] = swapNcomp[1]+1
		A[k] = left[i]
		i = i + 1
		k = k + 1
	while j < len(right): #compare++
		swapNcomp[1] = swapNcomp[1]+1
		A[k] = right[j]
		j = j + 1
		k = k + 1
	
def heap(A):
	#make_heap, heapify
	make_heap(A)
	
	n = len(A)
	for i in range(n, 0, -1):
		swap(A, 0, n-1) #swap++
		swapNcomp[0] = swapNcomp[0]+1
		n = n - 1
		heapify(A,n,0)
		
def make_heap(A):
	n = len(A)
	for i in range(n/2, -1, -1):
		heapify(A, n, i)
		
		
def heapify(A, n, i):
	while (2*i+1) < n: #compare++
		swapNcomp[1] = swapNcomp[1]+1
		L = 2*i + 1
		R = 2*i + 2
		if (A[i] < A[L]) : #compare++
			swapNcomp[1] = swapNcomp[1]+1
			m = L
		else: m = i
		if (R < n) and (A[m] < A[R]): #compare+2
			swapNcomp[1] = swapNcomp[1]+2
			m = R
		if i != m: #compare++
			swapNcomp[1] = swapNcomp[1]+1
			swap(A,i,m)
			i = m
		else: #compare++
			swapNcomp[1] = swapNcomp[1]+1
			break

def findMaxDigit(A): #compare is not included for this function.
	#return the maximum value in the array A
	max = A[0]
	digit = 0
	for i in range(len(A)):
		if(max < A[i]): max = A[i]
	while max > 0:
		max = max/10
		digit = digit + 1
	return digit
	
def radix(A):
	#radix sort 
	digit = findMaxDigit(A)
	temp = [[] for i in range(10)]
	
	#sorting for the 1's digit first for setting temp list
	for i in range(len(A)):
		value = A[i]%10
		for j in range(10):
			if(value == j): #compare++
				swapNcomp[1] = swapNcomp[1]+1
				temp[j].append(A[i])
	
	#Sorting starts from 10's digit to N's digit
	rep = 2
	while rep <= digit: #compare++
		swapNcomp[1] = swapNcomp[1]+1
		eachsize = [0]* 10
		for i in range (len(temp)):
			eachsize[i] = len(temp[i])
		for i in range(10):
			leng = eachsize[i]
			while(leng != 0): #compare++
				swapNcomp[1] = swapNcomp[1]+1
				value = temp[i].pop(0)
				for j in range(10):
					if(nthDigit(value, rep) == j): #compare++
						swapNcomp[1] = swapNcomp[1]+1
						temp[j].append(value)
				leng = leng - 1
		rep = rep + 1
	
	#copy temp to A
	j = 0
	for i in range(len(temp)):
		leng = len(temp[i])
		while leng > 0:
			value = temp[i].pop(0)
			A[j] = value
			j = j + 1
			leng = leng - 1

def nthDigit(value, rep):
	#Return the number of nth digit of value
	if rep == 0: return 0
	divider = 10
	while(rep-1 > 0):
		value = value/10
		rep = rep-1
	return value%10
	
def generateSortTxt():
	#Generate random numbers in txt file
	import random
	random.seed()
	in_file = open('sort.txt', 'w')
	n = int(raw_input("n = "))
	in_file.write(str(n)+'\n')
	for i in range(n):
		p = random.randint(0,200)
		in_file.write(str(p)+' ')
	in_file.close()

def setTheArray():
	#Store numbers in the list A and return
	in_file = open('sort.txt', 'r')
	num_of_data = int(in_file.readline())
	i = 0
	B = in_file.readline()
	B = B.split()
	A = []
	while i < num_of_data:
		value = int(B[i])
		#print value
		A.append(value)
		i = i + 1
	return A
	
def initialize(B):
	#This is for reinitializing the unsorted list B
	A = []
	for i in range(len(B)):
		A.append(B[i])
	return A
	
def sortAnalysis(sortType, swapp, comp, timeTaken):
	print "|%11s|%11d|%15d|%12f|" %(sortType, swapp, comp, timeTaken)
	
#generateSortTxt()
B = setTheArray()
#print "----------------------------------------------------"
#print "| SORT_TYPE |   SWAP#   |    COMPARE#   | TIME_TAKEN |"

A = initialize(B)
#swapNcomp[0], swapNcomp[1] = 0, 0
#start = time.clock()
selection(A)
#end = time.clock()
print check_sort(A)
#sortAnalysis("SELECTION", swapNcomp[0], swapNcomp[1], end-start)

A = initialize(B)
#swapNcomp[0], swapNcomp[1] = 0, 0
#start = time.clock()
insertion(A)
#end = time.clock()
print check_sort(A)
#sortAnalysis("INSERTION", swapNcomp[0], swapNcomp[1], end-start)

A = initialize(B)
#swapNcomp[0], swapNcomp[1] = 0, 0
#start = time.clock()
bubble(A)
#end = time.clock()
print check_sort(A)
#sortAnalysis("BUBBLE", swapNcomp[0], swapNcomp[1], end-start)

A = initialize(B)
#swapNcomp[0], swapNcomp[1] = 0, 0
#start = time.clock()
quick(A)
#end = time.clock()
print check_sort(A)
#sortAnalysis("QUICK", swapNcomp[0], swapNcomp[1], end-start)

A = initialize(B)
#swapNcomp[0], swapNcomp[1] = 0, 0
#start = time.clock()
merge(A)
#end = time.clock()
print check_sort(A)
#sortAnalysis("MERGE", swapNcomp[0], swapNcomp[1], end-start)

A = initialize(B)
#swapNcomp[0], swapNcomp[1] = 0, 0
#start = time.clock()
heap(A)
#end = time.clock()
print check_sort(A)
#sortAnalysis("HEAP", swapNcomp[0], swapNcomp[1], end-start)

A = initialize(B)
#swapNcomp[0], swapNcomp[1] = 0, 0
#start = time.clock()
radix(A)
#end = time.clock()
print check_sort(A)
#sortAnalysis("HEAP", swapNcomp[0], swapNcomp[1], end-start)
	

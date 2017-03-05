#open text file called 'gcd.txt'
file = open("gcd.txt", "r")

#read the first line(# of data)
num_of_data = int(file.readline())
i = 0
while i < num_of_data :
	line = file.readline()
	a, b = line.split()
	a = int(a)
	b = int(b)
	#GCD algorithm
	while a != 0 and b != 0:
		if a > b:
			a = a%b
		else:
			b = b%a
		
	print a+b
	i = i + 1
	
#close file	
file.close()
	

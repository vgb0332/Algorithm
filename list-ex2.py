input = raw_input()
input = input.split()

i = 0
for element in input:
	input[i] = int(element)
	i = i + 1
	
max = input[0]
min = input[0]

for element in input:
	if element > max:
		max = element
	elif element < min:
		min = element

print("%d" % max)
print("%d" % min)
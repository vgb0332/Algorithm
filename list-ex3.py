F0 = 0 
F1 = 1

F = [F0, F1]

n = raw_input()
n = int(n)

if n == 0:
	print F[0]
elif n == 1:
	print F[1]
else:
	i = 2
	while i <= n:
		value = F[(len(F)-1)] + F[(len(F)-2)]
		F.append(value)
		i = i+1
	print F[len(F)-1]


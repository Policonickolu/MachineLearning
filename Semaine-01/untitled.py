def func(lst, n):
	new = []
	while n > 0:
		new += lst
		n -= 1
	return new

print func([1,2,3], 1)
print func([1,2,3], 2)
print func([1,2,3], 3)
print func([1,2,3], 4)
print func([1,2,3], 5)

i = 0
while C[i] != None:
	print C[i]
	i += 1



def func3(str):
	for char in str:
		if str.count(char) == 1:
			return char


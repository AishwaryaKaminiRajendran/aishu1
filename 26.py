w=int(input())
e=[int(i) for i in input().split()]
a=sorted(e)
for i in range(0,len(e)):
	print(a[i],' ',end=" ")

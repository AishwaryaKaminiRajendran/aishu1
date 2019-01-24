w=int(input())
e=[int(i) for i in input().split()]
k=sorted(e)
for i in range(0,len(e)):
	print(k[i],end=" ")

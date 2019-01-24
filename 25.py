a=int(input())
b=[int(i) for i in input().split()]
y=sorted(b)
for i in range(0,len(b)):
	m=len(y)//2
print(y[m])

N=int(input())
i=1
c=0
while i<=N:
	if N%i==0:
		c=c+1
	i=i+1
if c==2:
	print("yes")
else:
	print("no")

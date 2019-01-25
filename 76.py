# your code goes here
a=int(input())
i=1
s=0
while i<=a:
	if a%i==0:
		s=s+1
	i=i+1
if s!=2:
	print("yes")
else:
	print("no")

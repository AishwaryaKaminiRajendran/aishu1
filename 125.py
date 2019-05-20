n=input()
a=list(n)

b=[]
for i in range(0,len(a)):
    if a.count(a[i])==1:
        b.append(a[i])

for j in range(0,len(b)):
    print(b[j],end="")

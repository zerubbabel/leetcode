def switch(row,n,a):
    minr=0
    for i in range(n):
        if a[row][i]<a[row][minr]:
            minr=i
    
    maxc=0
    for i in range(n):
        if a[i][row]>a[maxc][row]:
            maxc=i

    a[row][minr],a[maxc][row]=a[maxc][row],a[row][minr]

n=int(input())
a=[]
for i in range(n):
    t=[int(x) for x in input().split()]
    a.append(t)
for i in range(n):
    switch(i,n,a)

for i in range(n):
    a[i].sort()

for i in range(n):
    for j in range(n-1):
        print(a[i][j],end=' ')
    print(a[i][-1])

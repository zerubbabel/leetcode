'''
4.进制转换2
输入一个十六进制数，转换成十进制后输出s
'''
x=input()#A6
n=len(x)
s=0
for i in range(n):
    if '0'<=x[i]<='9':
        s=s+int(x[i])*16**(n-i-1)
        s=s*16+int(x[i])
    else:
        #A-F=>10-15
        s=s+(ord(x[i])-ord('A')+10)*16**(n-i-1)
        s=s*16+ord(x[i])-ord('A')+10

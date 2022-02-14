'''
3.进制转换1
输入一个二进制数，转换成十进制后输出
10011->19
'''
x=input()
n=len(x)
s=0
for i in range(n):
    #s+=int(x[i])*2**(n-i-1)
    s=s*2+int(x[i])
    print(s)
print(s)


'''
5.进制转换3
输入一个十进制数，转换成二进制后输出
13=>1101
'''
n=int(input())
s=''
while n>0:
    r=n%2
    n=n//2
    s=str(r)+s
print(s)
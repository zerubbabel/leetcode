'''倒序数:输入一个非负整数n，输出它的倒序数
如输入3080,输出803
'''
s=int(input())
x=0
while s>0:
    r=s%10
    s//=10
    x=x*10+r
print(x)



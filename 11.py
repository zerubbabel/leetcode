#斐波那契数列
#从第三项开始，每一项都是前两项之和
#0，1，1，2，3，5，8，13，。。。
#请你输出斐波那契数列的前n项
a,b=0,1
n=int(input())
for i in range(3,n+1):
    c=a+b
    a=b
    b=c
    print(c,end=' ')

    
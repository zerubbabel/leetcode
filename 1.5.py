'''
6.进制转换4
输入一个十进制数，转换成十六进制后输出
46=>2E
'''
n=int(input())
s=''
while n>0:
    r=n%16
    n//=16
    if r>9:
        #r:10-15=>'A'-'F'
        s=chr(r+ord('A')-10)+s
    else:
        s=str(r)+s
print(s)
def fbi(n):
    if n==1 or n==2:
        return 1
    else :
        return fbi(n-1)+fbi(n-2)
n=int(input("输入斐波那契位数："))
for i in range(1,n+1):
    print(fbi(i))

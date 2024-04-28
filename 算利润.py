i=int(input("输入净利润(万)："))
lr=[100,60,40,20,10,0]
a=[0.01,0.015,0.03,0.05,0.075,0.1]
r=0
for k in range(0,6):
    if lr[k]<i:
        r=r+(i-lr[k])*a[k]
print(r)


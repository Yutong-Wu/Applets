'''
古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月
后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
'''

n,a,b=1,0,1
while n<=15:
    print('第{}月，有兔子{}只'.format(n,b*2))
    a , b = b,a+b
    n +=1
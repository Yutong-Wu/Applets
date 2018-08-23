'''题目3：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
a = 整数
a + 100 = b**2
a + 100 +168 = c ** 2
'''
import math
def complete_square_number():
    n = -100
    while n < 1000000:
        x = int(math.sqrt(n+100))
        y = int(math.sqrt(n+268))
        if x**2 == n+100 and  y**2 == n+268:
            print(n)
        n +=1

complete_square_number()

# for x in range(1,1000):
#     a = int(math.sqrt(x+100))
#     b = int(math.sqrt(x+268))
#     if a * a== x+100 and b*b == x + 268:
#         print(x)

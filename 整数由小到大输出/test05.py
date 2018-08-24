'''题目5：输入三个整数x,y,z，请把这三个数由小到大输出。
x>y>z
x>z>y
y>x>z
y>z>y
z>y>x
z>x>y
'''
def integer(x,y,z):
    #自己想的方法
    # if x > y >z:
    #     print(z,y,x)
    # elif x > z> y:
    #     print(y,z,x)
    # elif y > x > z:
    #     print(z,x,y)
    # elif y > z > x:
    #     print(x,z,y)
    # elif z > y > x:
    #     print(x,y,z)
    # else:
    #     print(y,x,z)
    #查到的方法
    if x>y:
        x,y = y,x
    elif x>z:
        x,z=z,x
    elif y>z:
        y,z = z,y
    print(x,y,z)

while True:
    try:
        x = int(input('请输入第一个整数x:'))
        y = int(input('请输入第一个整数y:'))
        z = int(input('请输入第一个整数z:'))
        integer(x, y, z)
        break
    except Exception:
        print('您输入的有误，请重新输入！')


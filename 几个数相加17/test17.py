'''s=a+aa+aaa+aaaa+aa…a的值，其中a是一个数字。例如2+22+222+2222+22222(此时
　　　共有5个数相加)，几个数相加有键盘控制。 '''
a = input('输入相加数：')
count = int(input('相加几次：'))

ret = []
for i in range(1,count + 1):
    ret.append(int(a * i))

print('{}='.format(sum(ret)),end='')


n = 1
c = 0
while n < count:
    s = str(a)*n
    print(s,end='+')
    # c += int(str(a) * count)
    # print(c)
    n+=1
print(str(a)*count)
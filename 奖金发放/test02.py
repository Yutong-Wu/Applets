'''
企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高
于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提
成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于
40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于
100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
i <=10,      10%i
20 >i>10     10%i+(i-10)7.5%
20>i>40      10%i+(i-10)7.5%+(i-20)5%
40>i>60      10%i+(i-10)7.5%+(i-20)5%+(i-40)3%
60>i>100     10%i+(i-10)7.5%+(i-20)5%+(i-40)3%+(i-60)1.5%
i>100        10%i+(i-10)7.5%+(i-20)5%+(i-40)3%+(i-60)1.5%+(i-100)1%
'''

def bouns(i):
    n = 0.1 * int(i)
    if int(i) <= 10:
        print('当月利润{}万元,应发奖金{:.2f}万元'.format(i,n))
    elif  10 < int(i) <=20:
        n_10_20 = n +((int(i)-10)*0.075)
        print('当月利润{}万元,应发奖金{:.2f}万元'.format(i,n_10_20))
    elif  20< int(i) <=40:
        n_20_40=n+((int(i)-10)*0.075)+((int(i)-20)*0.05)
        print('当月利润{}万元,应发奖金{:.2f}万元'.format(i,n_20_40))
    elif  40 < int(i) <= 60:
        n_40_60=n + ((int(i) - 10) * 0.075) + ((int(i) - 20) * 0.05)+((int(i) - 40) * 0.03)
        print('当月利润{}万元,应发奖金{:.2f}万元'.format(i,n_40_60))
    elif  60 < int(i) <= 10:
        n_60_100=n + ((int(i) - 10) * 0.075) + ((int(i) - 20) * 0.05)+((int(i) - 40) * 0.03)+((int(i) - 60) * 0.015)
        print('当月利润{}万元,应发奖金{:.2f}万元'.format(i,n_60_100))
    else:
        n_100 = n + ((int(i) - 10) * 0.075) + ((int(i) - 20) * 0.05) + ((int(i) - 40) * 0.03) + (
                    (int(i) - 60) * 0.015)+((int(i) - 100) * 0.01)
        print('当月利润{}万元,应发奖金{:.2f}'.format(i,n_100))

i = input('当月利润:')
while True:
    if i.isdigit():
        bouns(i)
        break
    else:
        i = input('您输入的有误,请重新输入:')

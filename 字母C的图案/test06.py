'''用*号输出字母C的图案。 '''
#自己的方法
for i in range(1,5):
    if i ==1 :
        print('{:^6}'.format('****'))
    elif i==2:
        print('{:<3}'.format('*'))
    elif i==3:
        print('{:<3}'.format('*'))
    # elif i==4:
    #     print('{:<3}'.format('*'))
    else:
        print('{:^6}'.format('****'))
#查到的方法
# print('*' * 10)
# for i in range(5):
#     print('*         ')
# print('*' * 10)

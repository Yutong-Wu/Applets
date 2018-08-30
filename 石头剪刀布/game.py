import random
print('''
输入格式为：石头，剪刀，布，或者‘end’退出
''')
di1={
    '0':'剪刀',
    '1':'石头',
    '2':'布',
}
while True:
    li1 = input('你出的：')
    if li1 in ( '石头' ,'布' ,'剪刀' , 'end'):
     #   print(type(li1))
        if li1=='end':
            break
        computer = str(random.randint(0,2))
        key1 = di1.get(computer)
        print('电脑出的是:{}'.format(key1))

        if li1==key1:
            print('厉害了，这局是平局。。。\n')
                
        elif li1=='剪刀':
            if key1=='石头':
                print('很遗憾。你输了。。。\n')
            else:
                print('恭喜你，你赢了。。。\n')
                    
        elif li1=='石头':
            if key1=='布':
                print('很遗憾。你输了。。。\n')
            else:
                print('恭喜你，你赢了。。。\n')
                    
        elif li1=='布':
            if key1=='剪刀':
                print('很遗憾。你输了。。。\n')
            else:
                print('恭喜你，你赢了。。。\n')
    else:
        print('你输入的格式有误，请从新输入。。')

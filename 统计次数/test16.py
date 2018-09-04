'''输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。'''

def str1(a):
    dict1 = dict()
    for i in a:
        dict1.update({str(i):a.count(i)})
    print(dict1)


str1('aaabbb44   ...eee##')

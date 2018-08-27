'''利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，
　　　60分以下的用C表示。 '''
corse=float(input('请输入成绩：'))
if 0 <= corse <= 100:
    if corse>=60:
        if  60<=corse <90:
            print('该同学成绩为B')
        elif corse>=90:
            print('该同学成绩为A')
    elif corse<60:
        print('该学生成绩为C')


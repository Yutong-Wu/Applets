#-*- coding=utf-8 -*-
import jieba
excludes = {'将军','却说','二人','不可','荆州','不能','如此','商议','如何'}
contns = open('三国演义.txt','r',encoding='UTF-8').read()
words = jieba.lcut(contns)

count={}
for word in words:
    if len(word)==1:
        continue
    elif word in excludes:
        continue
    elif word=="孟德" or word=="丞相":
        new_word = "曹操"
    elif word=="孔明" or word=="孔明曰":
        new_word = "诸葛亮"
    elif word=="玄德" or word=="玄德曰":
        new_word = "刘备"
    elif word=="关公" or word=="云长":
        new_word = "关羽"
    else:
        new_word = word
    count[new_word] = count.get(new_word,0)+1

hits = list(count.items())
hits.sort(key=lambda x : x[1] ,reverse=True)

for i in range(15):
    word ,num = hits[i]
    print('{:<10}---{:>5}'.format(word,num))
from django.test import TestCase

# Create your tests here.
fulltxt = "홍길동 홍길동 아자"
strlength = len(fulltxt)  # 글자 수
words = fulltxt.split(" ")  # 단어들
wordcnt = len(words)  # 단어 수
word_dic = dict()  # 빈 딕셔너리 -> {'홍길동':2, '아자':1}

for word in words:
    print(word_dic.keys())
    if word in word_dic.keys():
        word_dic[word] += 1
    else:
        word_dic[word] = 1

print(fulltxt)
print("글자 수 :", strlength)
print("단어들 :", words)
print("단어 수 :", wordcnt)
# print("출현 단어(딕셔너리) : ", word_dic)
print("출현 단어(리스트) : ", word_dic.items())

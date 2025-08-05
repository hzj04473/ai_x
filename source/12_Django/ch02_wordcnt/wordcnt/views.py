from pickletools import read_uint1
from django.shortcuts import render

# Create your views here.


def wordinput(request):
    return render(request, "wordcnt/wordinput.jinja.html")


def about(request):
    return render(request, "wordcnt/about.jinja.html")


def result(request):
    """fulltxt 파라미터값 받아 글자수, 단어수, 출현단어등을 templates(result.jinja.html) 전송"""

    # POST 방식으로 전송
    # print("★ ", request.POST)
    # fulltxt = request.POST['fulltxt']
    # fulltxt = request.POST.get("fulltxt", "")

    # GET 방식으로 전송
    fulltxt = request.GET.get("fulltxt", "")

    strlength = len(fulltxt)  # 글자 수
    words = fulltxt.split(" ")  # 단어들
    wordcnt = len(words)  # 단어 수
    words_dic = dict()  # 빈 딕셔너리 -> {'홍길동':2, '아자':1}

    for word in words:
        # print(word_dic.keys())
        if word in words_dic.keys():
            words_dic[word] += 1
        else:
            words_dic[word] = 1

    context = {
        "fulltxt": fulltxt,
        "strlength": strlength,
        "wordcnt": wordcnt,
        "dict": words_dic.items(),
    }

    return render(
        request=request, template_name="wordcnt/result.jinja.html", context=context
    )

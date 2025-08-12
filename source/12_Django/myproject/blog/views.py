import re
from django.shortcuts import render
from django.http import JsonResponse  # HttpResponse 하위클래스
from .models import Post


# Create your views here.
def index(request):
    return JsonResponse(
        {"singer": "BTS", "song": ["DNA", "FAKE LOVE", "피땀눈물"]},
        json_dumps_params={"ensure_ascii": False},
    )


def list(request):
    post_list = Post.objects.all()
    return render(
        request=request,
        template_name="blog/index.jinja.html",
        context={"post_list": post_list},
    )


def detail(request, post_id: int):
    """게시글 상세 페이지 뷰"""
    try:
        # post = Post.objects.get(id=post_id)
        post = Post.objects.get(pk=post_id)
        return render(
            request=request,
            template_name="blog/detail.jinja.html",
            context={"post": post},
        )

        # post = Post.objects.filter(pk=post_id)  # 조건에 맞는 데이터를 list 만듬

        # if post:
        #     return render(
        #         request=request,
        #         template_name="blog/detail.jinja.html",
        #         context={"post": post[0]},
        #     )
        # else:
        #     message.error(request, "게시글을 찾을 수 없습니다.")
        #     return redirect("blog:index")

    except Post.DoesNotExist:
        # 게시글이 존재하지 않을 경우 404 에러 처리
        from django.http import Http404

        raise Http404("게시글을 찾을 수 없습니다.")

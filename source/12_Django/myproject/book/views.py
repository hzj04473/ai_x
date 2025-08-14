from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import BookModelForm
from .models import Book

# 1. form없이 걍 2. form객체생성후(6장) 3. DjangoGenericView 이용 4. GenericView 상속(7장)


# 1.
# def book_list(request):
#     return render(request, "book/book_list.jinja.html", {"book_list": Book.objects.all()})

book_list = ListView.as_view(model=Book, template_name="book/book_list.jinja.html")

# GET : template / POST : 파라미터 변수 받아 db에 save -> book: book_list
def book_new(request):
    if request.method == "POST":
        # title = request.POST.get("title")
        # author = request.POST.get("author")
        # publisher = request.POST.get("publisher")
        # sales = int(request.POST.get("sales"))
        # ip = request.META.get("REMOTE_ADDR")  # 요청한 client ip
        # book = Book(title=title, author=author, publisher=publisher, sales=sales, ip=ip)
        # book.save()
        # return redirect("book:book_list")
        # return redirect(book)  # book.get_absolute_url의 return 값으로 이동
        form = BookModelForm(request.POST)
        # print("⭐️", form.is_valid())  # 유효성 검증 결과
        # print("유효성 검사 결과 : ", form.cleaned_data)

        if form.is_valid():  # 유효성 검사
            book = Book(**form.cleaned_data)
            book.ip = request.META.get("REMOTE_ADDR")
            book.save()
            return redirect(book)
        else:
            return render(request, "book/book_form.jinja.html", {"form": form})
    elif request.method == "GET":
        form = BookModelForm()
        return render(request, "book/book_form.jinja.html", {"form": form})

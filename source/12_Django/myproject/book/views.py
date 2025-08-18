from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import BookModelForm
from .models import Book

# 1. form없이 걍 2. form객체생성후(6장) 3. DjangoGenericView 이용 4. GenericView 상속(7장)


# 1.
# def book_list(request):
#     return render(request,
#     "book/book_list.jinja.html",
#     {"book_list": Book.objects.all()})

book_list = ListView.as_view(model=Book, template_name="book/book_list.jinja.html")


class BookCreateView(CreateView):
    model = Book
    fields = ["title", "author", "publisher", "sales"]
    template_name = "book/book_form.jinja.html"

    def form_valid(self, form):
        book = form.save(commit=False)
        book.ip = self.request.META.get("REMOTE_ADDR")
        book.save()
        return redirect(book)


book_new = BookCreateView.as_view()

# book_new = CreateView.as_view(
#    model=Book, fields=["title", "author", "publisher", "sales"]
# )


# GET : template / POST : 파라미터 변수 받아 db에 save -> book: book_list
def book_new1(request):
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

            # book = Book(**form.cleaned_data)
            # book.ip = request.META.get("REMOTE_ADDR")

            book = form.save(commit=False)
            book.ip = request.META.get("REMOTE_ADDR")

            book.save()

            # return redirect(book)
        # else:
        #     return render(request, "book/book_form.jinja.html", {"form": form})
    elif request.method == "GET":
        form = BookModelForm()
    return render(request, "book/book_form.jinja.html", {"form": form})


class BookUpdateView(UpdateView):
    model = Book
    fields = ["title", "author", "publisher", "sales"]
    template_name = "book/book_form.jinja.html"

    def form_valid(self, form):
        book = form.save(commit=False)
        book.ip = self.request.META.get("REMOTE_ADDR")
        book.save()
        return redirect(book)


book_edit = BookUpdateView.as_view()

# book_edit = UpdateView.as_view(
#     model=Book, fields=["title", "author", "publisher", "sales"]
# )


def book_edit1(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookModelForm(request.POST, instance=book)
        if form.is_valid():
            form.save()  # 수정시 ip 수정 X
            # form save(False)
            # book.ip = request.META.get("REMOTE_ADDR")
            # book.save()
            return redirect(book)
    else:
        form = BookModelForm(instance=book)
    return render(request, "book/book_form.jinja.html", {"form": form})


# class BookDeleteView(DeleteView):
#     model = Book
#     success_url = reverse_lazy("book:book_list")


# book_delete = BookDeleteView.as_view()


book_delete = DeleteView.as_view(
    model=Book,
    template_name="book/book_confirm_delete.jinja.html",
    success_url=reverse_lazy("book:book_list"),
)


def book_delete1(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book:book_list")
    elif request.method == "GET":
        return render(request, "book/book_confirm_delete.jinja.html", {"object": book})

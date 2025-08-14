from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
    path("", views.book_list, name="book_list"),
    path("new/", views.book_new, name="book_new"),
]

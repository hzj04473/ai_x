from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
    path("", views.book_list, name="book_list"),
    path("new/", views.book_new, name="book_new"),
    path("<int:pk>/edit/", views.book_edit, name="book_edit"),
    path("<int:pk>/delete/", views.book_delete, name="book_delete"),
]

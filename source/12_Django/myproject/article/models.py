import os.path
from django.db import models
import time
from datetime import datetime
from django.urls import reverse
from myproject import settings
from django.shortcuts import get_object_or_404

STATUS_CHOICES = (
    ("", "---------"),
    ("d", "Draft"),
    ("p", "Published"),
    ("w", "Withdrawn"),
)


class Article(models.Model):
    title = models.CharField(verbose_name="제목", max_length=100)
    content = models.TextField(verbose_name="본문")
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default="d"
    )  # select
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse("article:list")
        return reverse("article:detail", args=[self.id])

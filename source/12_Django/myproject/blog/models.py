from django.db import models
import re
from django.core.exceptions import (
    ValidationError,
)  # 변경: forms가 아니라 core.exceptions

REGION_CHOICE = (
    ("Europe", "유럽"),
    ("Asia", "아시아"),
    ("Oceania", "오세아니아"),
    ("America", "아메리카"),
)


def lnglat_validator(value: str):
    # 예: "38.8, 128.8" 형태(공백 허용, 음수 허용)
    if not re.match(r"^\s*-?\d+(\.\d+)?\s*,\s*-?\d+(\.\d+)?\s*$", value or ""):
        raise ValidationError("Invalid LngLat. ex: 38.8, 128.8")


class Post(models.Model):  # 테이블명: blog_post
    # id는 기본 PK 자동 생성
    title = models.CharField(
        "제목", max_length=100, help_text="제목을 입력하세요. 100자 내외"
    )
    content = models.TextField("본문")
    created_at = models.DateField(auto_now_add=True)  # 필드명 정리
    update_at = models.DateTimeField(auto_now=True)
    region = models.CharField(
        verbose_name="지역", max_length=20, choices=REGION_CHOICE, default="Asia"
    )
    lnglat = models.CharField(
        "위도/경도",
        max_length=20,
        blank=True,
        null=True,
        help_text="위도/경도 정보를 입력하세요. 예: 38.8, 128.8",
        validators=[lnglat_validator],
    )

    url = models.URLField(verbose_name="URL", blank=True, null=True)

    def __str__(self):
        return f"제목 : {self.title} - {self.created_at} 작성 {self.update_at} 최종수정"

    class Meta:
        ordering = ["-update_at"]


class Comment(
    models.Model
):  # 테이블명 : blog_commnet (Post의 댓글 내용-post:commnet=1:N)
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE
    )  # post 내용을 delete 할 경우 자동 삭제 (on_delete=models.CASCADE)
    author = models.CharField(
        verbose_name="작성자", max_length=20, null=True, blank=True
    )
    message = models.TextField(verbose_name="댓글")
    create_at = models.DateTimeField(verbose_name="작성일시", auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="최종수정일시", auto_now=True)

    def __str__(self):
        return (
            f"댓글 : {self.message} - {self.create_at} 작성 {self.update_at} 최종수정"
        )

    class Meta:
        ordering = ["-create_at", "-update_at"]

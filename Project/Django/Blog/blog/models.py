from django.db import models


# Create your models here.
class Blog(models.Model):
    CATEGORY_CHOICES = (
        ("free", "자유"),
        ("travle", "여행"),
        ("cat", "고양이"),
        ("dog", "강아지"),
    )

    category = models.CharField("카테고리", max_length=10, choices=CATEGORY_CHOICES)
    title = models.CharField("제목", max_length=100)
    content = models.TextField("본문")

    created_at = models.DateTimeField("작성일자", auto_now_add=True)
    updated_at = models.DateTimeField("작성일자", auto_now=True)

    # 제목이 노출되는 형식을 설정합니다. [카테고리] 제목은 최대 10자까지
    def __str__(self):
        return f"[{self.get_category_display()}] {self.title[:10]}"

    # Meta 클래스 코드 추가
    class Meta:
        verbose_name = "블로그"
        verbose_name_plural = "블로그 목록"

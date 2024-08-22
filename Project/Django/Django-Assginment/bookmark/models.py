from django.db import models


# Create your models here.
class Bookmark(models.Model):
    name = models.CharField("이름", max_length=100)
    url = models.URLField("URL")
    create_at = models.DateTimeField(verbose_name="생성일시", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정일시", auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Bookmark"
        verbose_name_plural = "Bookmark_list"

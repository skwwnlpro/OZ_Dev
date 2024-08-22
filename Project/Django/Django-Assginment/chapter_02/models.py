from django.db import models


# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "To-Do"
        verbose_name_plural = "To-Do list"

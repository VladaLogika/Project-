from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # Додаємо User для автора
# create models here!!

class Category(models.Model):
    name = models.CharField(max_length=100)

    def  __str__ (self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):

        return self.title
    
class Comment(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name="Ім'я"
    )
    email = models.EmailField(
        verbose_name="Email",
        blank=True
    )
    text = models.TextField(
        verbose_name="Коментар"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата"
    )


    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"
        ordering = ['-created_at']

    def __str__(self):
        return self.name


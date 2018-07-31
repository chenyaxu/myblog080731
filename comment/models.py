from django.db import models

# Create your models here.
from django.urls import reverse


class Comment(models.Model):
    name = models.CharField(max_length=50, verbose_name='姓名')
    email = models.EmailField(verbose_name='邮箱')
    url = models.URLField(verbose_name='网址')
    content = models.TextField(verbose_name='内容')
    create_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return self.content[:20]



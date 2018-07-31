import markdown
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.html import strip_tags


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='标题')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    excerpt = models.CharField(max_length=300, verbose_name='摘要', null=True, blank=True)
    content = models.TextField(verbose_name='正文')
    author = models.ForeignKey(User, verbose_name='作者')
    category = models.ForeignKey('Category', verbose_name='类别')
    tags = models.ManyToManyField('Tag', verbose_name='标签')
    # 阅读数
    views = models.PositiveIntegerField(verbose_name='阅读数', default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_time']

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.id})

    def creates_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite'
            ])
            self.excerpt = strip_tags(md.convert(self.content))[:54]
            super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='类别')

    def __str__(self):
        return self.name


class Tag(models.Model):
    tag_name = models.CharField(max_length=20, verbose_name='标签')

    def __str__(self):
        return self.tag_name

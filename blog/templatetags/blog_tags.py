from django import template
from django.db.models import Count

from blog.models import Post, Category, Tag

register = template.Library()


# 获取最新文章
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-create_time')[:num]


# 归档
@register.simple_tag
def archives():
    return Post.objects.dates('create_time', 'month', order='DESC')


# 分类
@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

# 标签
@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

import markdown
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from  comment.forms import commentModelForm

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView

from blog.models import Post, Category, Tag


def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {'post_list': post_list})


class postListView(ListView):
    model = Post
    template_name = 'blog/index.html'


def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.content = markdown.markdown(post.content,
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc', ])
    forms = commentModelForm()
    comment_list = post.comment_set.all()
    post.creates_views()
    return render(request, 'blog/post_detail.html', {'post': post, 'forms': forms, 'comment_list': comment_list})


# 归档
def archives(request, year, month):
    post_list = Post.objects.filter(create_time__year=year,
                                    create_time__month=month
                                    ).order_by('-create_time')
    return render(request, 'blog/index.html', {'post_list': post_list})


# 分类
def category(request, id):
    print('测试')
    category = Category.objects.get(id=id)
    post_list = Post.objects.filter(category=category).order_by('-create_time')
    return render(request, 'blog/index.html', {'post_list': post_list})


# 标签云
def post_tags(request, id):
    tag = Tag.objects.get(id=id)
    post_list = Post.objects.filter(tags=tag).order_by('-create_time')
    return render(request, 'blog/index.html', {'post_list': post_list})


# 搜索功能
def search(request):
    q = request.GET.get('q', None)
    if q:
        post_list = Post.objects.filter(
            Q(title__contains=q) | Q(content__contains=q) | Q(author__first_name__contains=q))
        return render(request, 'blog/index.html', {'post_list': post_list})
    else:
        msg = '请输入搜索关键字'
        return render(request, 'blog/index.html', {'msg': msg})

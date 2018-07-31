from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

# Create your views here.
from django.urls import reverse

from blog.models import Post
from comment.forms import commentModelForm


def get_comment(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = commentModelForm(request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.post = post
            comments.save()
        else:
            context = {
                'post': post,
                'form': form,
                'comment_list': post.comment_set.all()
            }
            return render(request, 'blog/post_detail.html', context)
    return redirect(post)

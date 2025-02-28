from django.shortcuts import render, get_object_or_404
# from django.http import Http404

from .models import Post


# Create your views here.
# The request paramer is required by all views.
def post_list(request):
    "List all published posts"
    posts = Post.published.all()

    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )

# def post_detail(request, id):
#     try:
#         post = Post.published.get(id=id)
#     except Post.DoesNotExist:
#         raise Http400("No post found")
#     return render(
#         request,
#         'blog/post/detail.html',
#         {'post': post}
#     )

# Next method simplify the render process using the Django shortcut get_object_or_404
def post_detail(request, id):
    post = get_object_or_404(
        Post,
        id=id,
        status=Post.Status.PUBLISHED
        )
    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )


from django.shortcuts     import render
from django.views.generic import ListView

from .models          import Post

# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#     return render(request, 'blog/index.html', {
#         'posts': posts,
#         }
#     )
class PostList(ListView):
    model = Post
    ordering = '-pk'
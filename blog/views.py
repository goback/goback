from django.shortcuts     import render
from django.views.generic import DetailView

from .models              import Post

# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)

#     return render(request, 'blog/single_post_page.html', {
#         'post' : post,
#     })
class PostDetail(DetailView):
    model = Post
from django.shortcuts     import render
from django.views.generic import ListView
from django.views.generic import DetailView

from .models              import Post, Category

class CategoryList(ListView):
    model         = Category
    template_name = 'blog/category_list.html'
    ordering      = '-pk'

class PostList(ListView):
    model    = Post
    ordering = '-pk'

    def get_queryset(self):
        return Post.objects.filter(category=self.kwargs['pk'])

# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)

#     return render(request, 'blog/post_detail.html', {
#         'post' : post,
#     })
class PostDetail(DetailView):
    model = Post
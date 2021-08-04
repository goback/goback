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

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['post_list'] = Post.objects.filter(category=self.kwargs['pk'])
        context['category_name'] = Category.objects.get(pk=self.kwargs['pk'])
        return context

# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)

#     return render(request, 'blog/post_detail.html', {
#         'post' : post,
#     })
class PostDetail(DetailView):
    model = Post
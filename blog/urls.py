from django.urls import path

from .views      import CategoryList, PostDetail, PostList

app_name = 'blog'

urlpatterns = [
    path('/category', CategoryList.as_view(), name='category_list'),
    path('/category/<int:pk>', PostList.as_view(), name='post_list'),
    path('/post/<int:pk>', PostDetail.as_view(), name='post_detail'),
]

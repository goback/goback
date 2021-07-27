from django.urls import path

from .views      import PostDetail, PostList

app_name = 'blog'

urlpatterns = [
    path('', PostList.as_view()),
    path('/<int:pk>', PostDetail.as_view(), name='detail'),
]

from django.urls import path
from .views      import PostDetail

app_name = 'blog'

urlpatterns = [
    path('/<int:pk>', PostDetail.as_view(), name='detail'),
]

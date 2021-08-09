from django.db        import models
from django.shortcuts import resolve_url

class Post(models.Model):
    title      = models.CharField(max_length=30)
    category   = models.ForeignKey("Category", on_delete=models.CASCADE)
    content    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'posts'

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return resolve_url('blog:post_detail', self.pk)

class Comment(models.Model):
    post       = models.ForeignKey(Post, on_delete=models.CASCADE)
    author     = models.CharField(max_length=50)
    content    = models.TextField()
    password   = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'

    def __str__(self):
        return f'{self.content}'

class Category(models.Model):
    name        = models.CharField(max_length=45, unique=True)
    title_image = models.ImageField(upload_to='blog/images/category/%Y/%m/%d/', blank=True)

    class Meta:
        db_table            = 'categories'
        verbose_name_plural = 'categories'

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return resolve_url('blog:post_list', self.pk)
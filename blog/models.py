from django.db        import models
from django.shortcuts import resolve_url

class Post(models.Model):
    title       = models.CharField(max_length=30)
    category_id = models.ForeignKey("Category", on_delete=models.CASCADE)
    content     = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'posts'

    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return resolve_url('blog:post_detail', self.pk)

class Category(models.Model):
    name = models.CharField(max_length=45, unique=True)

    class Meta:
        db_table            = 'categories'
        verbose_name_plural = 'categories'

    def __str__(self):
        return f'[{self.pk}]{self.name}'

    def get_absolute_url(self):
        return resolve_url('blog:post_list', self.pk)
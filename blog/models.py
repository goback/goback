from django.db import models

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

class Category(models.Model):
    name = models.CharField(max_length=45, unique=True)

    class Meta:
        db_table = 'categories'
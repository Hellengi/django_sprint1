from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(
        Category,
        related_name='posts',
        on_delete=models.CASCADE,
    )
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

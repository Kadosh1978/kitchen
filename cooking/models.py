from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(default='Скоро тут будет статья!')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    watched = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

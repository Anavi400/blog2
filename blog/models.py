from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(
        "auth.user",
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return self.title


# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     text = models.TextField()
#     author = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self) -> str:
#         return self.text
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.content[:20]}'
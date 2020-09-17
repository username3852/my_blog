from django.db import models
from django.utils import timezone  # inorder to make changes in post created time
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='blog_pics')
    content = models.TextField()
    # imported above to change the created time whenever desired
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

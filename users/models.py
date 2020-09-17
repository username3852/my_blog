from django.db import models
from django.contrib.auth.models import User
from PIL import Image  # to scale the image in good size


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # default means that if we don't have image then we will use as default

    def __str__(self):
        return (f"{self.user.username} Profile")

    # this method is for the scaling of the image
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)  # opens the image of that instance

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

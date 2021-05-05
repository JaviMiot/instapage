from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    """proxy models
    proxy model taht extends the base data with
    other infromation
    Args:
        models ([type]): [description]
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(max_length=200, blank=True)
    bigography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    picture = models.ImageField(
        upload_to='users/pictures', blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

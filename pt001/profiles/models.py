from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    gender_choices = ((0, 'Female'),
                      (1, 'Male'))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_pics')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    dob = models.DateField(null=True)
    gender = models.IntegerField(choices=gender_choices)

    def __str__(self):
        return self.user.username

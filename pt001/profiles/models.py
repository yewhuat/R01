from django.db import models

class Profile(models.Model):
    gender_choices = (('0', 'Female'),
                      ('1', 'Male'))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=user_directory_path)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    dob = models.DateField(null=True)
    gender = models.IntegerFieldchoices=gender_choices)

    def __str__(self):
        return self.user.username

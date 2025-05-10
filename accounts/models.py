from django.db import models
from django.urls import reverse
# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('user-page', args=[self.username])

class Authorization(models.Model):
    authorization_id = models.AutoField(primary_key=True)
    hashed_password = models.CharField(max_length=64) #SHA-512 generates 512-bit value (biggest one)
    hash_method = models.CharField(max_length=12)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Authorization"
        verbose_name_plural = "Authorizations"

    def __str__(self):
        return str(self.user.username) + "`s  Authorization"


from django.db import models

from django.contrib.auth.models import AbstractUser,Group, Permission
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser,User

from app.models import User


class User(AbstractUser):
    # Custom fields
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    username = models.CharField(max_length=100 ,unique=True)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField(null=True)
    is_doctor = models.BooleanField('Is doctor',default=False)
    is_patient = models.BooleanField('Is patient',default=False)
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='app_user_groups')
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='app_user_permissions'
    )


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    Title = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='blog_images')
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Summary = models.TextField(max_length=200)
    Content = models.TextField(max_length=200)
    is_draft = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title
 


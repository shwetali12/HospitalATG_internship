from django.contrib import admin
from django.contrib.auth.admin import User
from .models import User,BlogPost,Category
admin.site.register(User)
admin.site.register(BlogPost)
admin.site.register(Category)


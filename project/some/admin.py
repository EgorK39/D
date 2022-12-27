from django.contrib import admin
from .models import UserModel, PostModel, Comment

admin.site.register(UserModel)
admin.site.register(PostModel)
admin.site.register(Comment)

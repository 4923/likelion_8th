from django.contrib import admin
from .models import Post, Comment # model 등록

admin.site.register(Post)
admin.site.register(Comment)
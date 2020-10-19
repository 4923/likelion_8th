from django.contrib import admin
from .models import Post

# Register your models here.

# admin에 Post라는 클래스 등록
admin.site.register(Post)
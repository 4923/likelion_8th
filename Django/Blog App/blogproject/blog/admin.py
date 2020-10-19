from django.contrib import admin
from .models import Post
# 같은 폴더에 위치한 models.py 파일로부터 Post를 가져옴

# Register your models here.
admin.site.register(Post)
# admin이라는 site에 Post라는 클래스를 등록(register)
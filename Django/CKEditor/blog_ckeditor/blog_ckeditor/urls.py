"""blog_ckeditor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import blogapp.views
# 하단 세개는 이미지 url 추가하기 위해 import 함
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.index, name='index'),
    # 경로에 아무것도 없을 때 ('') index를 불러오고 이 과정을 index라고 이름붙인다.
    path('blogMain/', blogapp.views.blogMain, name='blogMain'),
    # 경로가 blogMain/ 이후일때 blogapp 이라는 앱의 views에서 blogMain을 불러오고 이 과정을 blogMain으로 이름붙인다.
    path('blogMain/createBlog/', blogapp.views.createBlog, name='createBlog'),
    path('ckeditor/', include('ckeditor_uploader.urls')), # 이미지 url 추가
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Add

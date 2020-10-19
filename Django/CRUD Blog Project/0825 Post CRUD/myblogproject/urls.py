"""myblogproject URL Configuration

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
from django.urls import path, include # urls 분리에 사용되는 include 추가 import
from django.conf.urls import url # 이거 안쓰면 밑에 url(''~~~) 부분에서 NameErro: name'url' is not defined 생김

urlpatterns = [
  path('admin/', admin.site.urls),
  url('', include('myblog.urls')),
]




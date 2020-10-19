"""blogproject URL Configuration

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
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    # [path-converter] 계층적 url이 필요할 때 사용, 모양 == <type:name>
    # '지정한 converter type의 name변수를 view 함수로 넘겨라'
    # int:post_id == 각 게시글의 id값이 들어갈 공간
    # 모든 게시글의 path를 적을 필요 없이, django는 각 게시글의 id를 전달받아 url을 디자인한다.
    path('<int:post_id>/', blog.views.detail, name="detail"),
    path('new/', blog.views.new, name="new"),
    path('create/', blog.views.create, name="create"),
]

# templates에서 가져오는 posts는 list형식. 슬라이싱 가능함.

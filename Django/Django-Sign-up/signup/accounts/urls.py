from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  # 회원가입과 로그인, 로그아웃 url 설정
  path('signup/', views.signup, name='signup'),
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
  path('userpage',views.userpage, name='userpage'),
  path('activate/<str:uidb64>/<str:token>/', views.activate, name="activate"),
]
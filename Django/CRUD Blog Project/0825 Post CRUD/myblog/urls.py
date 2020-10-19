# 기본 path 함수를 사용하기 위해 import
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# project의 urls.py는 어떤 app의 views인지 알기 위해 blog.views 먼저 썼지만
# 여기서는  그럴 필요가 없고 동일한 폴더 안의 views임을 명시해야 하므로
# from . 에서 . 는 현재폴더
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create10/', views.create10, name='create10'),
    path('<int:post_id>/', views.details, name="detail"),
    path('new/', views.new, name="new"),
    path('<int:post_id>/edit/', views.edit, name='edit'),
    path('<int:post_id>/delete/', views.delete, name="delete"),
    path('<int:post_id>/comments/create/', views.comments_create, name='comments_create'),
    path('<int:post_id>/comments/<int:comment_id>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:post_id>/comments/<int:comment_id>/update/', views.comments_update, name='comments_update'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# project의 urls.py는
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
# 이랬었음. App 안의 urls.py는 어떤 App 안의 views 인지 알리는 부분이 빠짐
# 'admin/' 이부분
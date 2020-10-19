from django.contrib import admin
from django.urls import path
# Apps
import blog.views # 이거 이렇게만 쓰면 자꾸 밑줄생기는데 뭐때문인지 모르겠음
import portfolio.views

# https://github.com/lee-sj/2020-django/blob/master/2020_08_08_handler_sorry.md
from django.conf import settings
from django.conf.urls.static import static

# <404 handler>
from django.conf.urls import handler404
import handlerpage.views

handler404 = 'handlerpage.views.handler404'

urlpatterns = [
  # admin page
    path('admin/', admin.site.urls),
  # blog home
    path('', blog.views.home, name="home"),
    path('<int:post_id>/', blog.views.detail, name="detail"),
    path('blog/create/', blog.views.create, name='create'),
    path('new/', blog.views.new, name="new"),
    # 이거 blog.views.detail이 아니라 delet였음어쩐지이상하다했다
    # https://tothefullest08.github.io/django/2019/04/27/Django07_CRUD4/
    path('<int:post_id>/delete',blog.views.delete, name='delete'),
  # portfolio
    path('portfolio/',portfolio.views.portfolio, name="portfolio")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# <int: post_id> 같은걸 path-converter라고 함
# django에서 여러 객체를 다루는 "계층적 url"이 필요할 때 사용하며
# <int: post_id>에 각 게시물의 id값이 할당된다.

# 형식: <type:name>
# 지정한 converter type의 name 변수를 view 함수로 넘겨라

# 이 외에도 converter에는 다양한 타입이 있음 -> 검색!
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  # 앱에서 만든 url을 프로젝트로 끌어오는게 아닌가?
  path('accounts/', include('accounts.urls'))
]

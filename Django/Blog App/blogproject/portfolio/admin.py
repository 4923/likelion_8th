from django.contrib import admin
from .models import Portfolio

# Register your models here.

# 모델만들고 등록하러왔음
admin.site.register(Portfolio)

# 런서버 해보니까
# ImportError: cannot import name 'Portfolio' from 'portfolio.models' (C:\Users\dmatm\OneDrive\ 
# 바탕 화면\2020\like lion\코딩 세션\Django\0818-20 blog app\blogproject\portfolio\models.py) 
# 이런 에러 나오는데 뭐지


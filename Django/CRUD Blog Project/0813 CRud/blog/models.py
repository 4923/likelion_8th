from django.db import models

# Create your models here.

# 1.
# 모델을 정의
# Post: 모델의 이름. 클래스 이름의 첫 글자는 대문자
# models: django 모델임을 의미. Post가 DB에 저장되어야함을 알림

class Post(models.Model):
  # 2. 하단은 각각 속성
  title = models.CharField(max_length=200)  # 문자를 title 변수로 받음
  pub_date = models.DateTimeField('date published') # 날짜와 시간 데이터 (published data)
  body = models.TextField() # char field 보다 더 긴 문자열

# title을 list에서 보여주기 (models.py)
  def __str__(self):
    return self.title
  
  def summary(self):
    return self.body[:20] # list slicing, body의 20번째 글자 전까지만 출력
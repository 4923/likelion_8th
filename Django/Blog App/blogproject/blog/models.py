from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    # DB 모델 만든 후에!!! migration 만드는거 잊지 말기
      # python manage.py makemigrations
    # DB에 적용하는것도 잊지 말기
      # python manage.py migrate
    
    def __str__(self):
      return self.title
      # self를 받아서 title을 반환해주기 때문에 제목이 보인다.
    
    # 보여질 글자 수 지정하기
    def summary(self):
      return self.body[:20]
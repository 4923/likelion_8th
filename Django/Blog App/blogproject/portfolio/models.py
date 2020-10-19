from django.db import models

# 모델 작성 후에 migration 잊지 말기

# Create your models here.
# class 이름의 첫글자는 대문자로
class Portfolio(models.Model):
  title = models.CharField(max_length=255)
  image = models.ImageField(upload_to='images/')
  # blog app과의 차이점: 이미지를 업로드한다.
  # 업로드된 이미지를 images 폴더 안에 넣으라는 의미
  # 이미지 처리하니까 Pillow 설치하기 (pip 업그레이드 전에 한거같은데 왜 또하라고...?)
  description = models.CharField(max_length=500)

  def __str__(self):
    return self.title


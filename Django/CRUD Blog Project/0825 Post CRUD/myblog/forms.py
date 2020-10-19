from django import forms  # model import
from .models import Post  # model(Post) import

class PostForm(forms.ModelForm):  
  # PostForm: 우리가 만들 폼의 이름
  # (forms.ModelForm)을 통해 이 폼이 ModelForm임을 알려줘야 함
  class Meta:
    # Form을 만들기 위한 model (=Post) 알려주기
    model = Post
    fields = ('title', 'body', 'image')
    # form에 field (어떤거 넣을지는 괄호 안에 적기)넣으면 끝

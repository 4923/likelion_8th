
from django import forms
from .models import Blog
from ckeditor_uploader.widgets import CKEditorUploadingWidget # 유저 글쓰기 페이지에 이미지 업로드 기능 구현중

class CreateBlog(forms.ModelForm):
    class Meta:
        model = Blog

        fields = ['title', 'pub_date', 'body']

        # 유저 글쓰기 페이지에 이미지 업로드 페이지 구현: 하단 widgets 추가
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
            ),
            'pub_date': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '작성일짜를 입력하세요.'}
            ),
            'body': forms.CharField(widget=CKEditorUploadingWidget()),
        }

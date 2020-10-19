# get_object_or_404: object를 가져오고 없을경우 404 에러를 띄워라.
# redirect 설명은 하단에
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post


# Create your views here.

# model에서 templates 로 바로 내용 보낼 수 없기 때문에 views.py를 작성
def home(request):
  # posts라는 변수에 Post 객체 (데이터들) 할당
  posts = Post.objects
  # {'posts':posts} : render의 세번째 parameter는 dict type. 데이터를 넘긴다
  # posts에 할당된 데이터를 'posts' 라는 이름으로 넘김.
  # -> template에서 posts라는 이름의 데이터를 다룸
  return render(request, 'home.html',{'posts':posts})

# Queryset, 쿼리셋 == 모델로부터 전달받은 객체목록
# Method, 메소드 == 쿼리셋을 처리하는 방법


def detail(request, post_id):
  # post_detail에 object를 담아 detail로 넘겨줌.
  # 여기서 게시글의 id = pk가 됨. => 'post' 변수에 담아 이동 됨
  
  # pk(primary key)란?
  # 모델에서 찍어낸 객체들을 구분할 수 있는 구분자
  post_detail = get_object_or_404(Post, pk=post_id)
  return render(request, 'detail.html', {'post' : post_detail})

def new(request):
  return render(request, 'new.html')

def create(request):
  post = Post()
  # new.html 파일의 form 태그 안에 있는 것.
  # name = 'title' 이기 때문에 get 안에 'title'이 들어감
  # form 태그의 해당 부분을 받겠다는 의미
  post.title = request.GET['title']
  post.body = request.GET['body']
  # 시간 자동 입력 (현재), timezone 패키지 사용 (위에 import 함)
  post.pub_date = timezone.datetime.now()
  post.save()
  # redirect: 요청 처리하고 보여주는 페이지. render가 요청에 따라 html을 보여준다면 redirect는 요청에 따라 특정 url로 전송한다. (첫줄에서 import 했음)
  return redirect('/' +str(post.id))
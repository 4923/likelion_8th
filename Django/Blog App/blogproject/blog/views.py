from django.shortcuts import render,  get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator # pagination 사전작업
from .models import Post  # views.py에 Post를 import

# Create your views here.
def home(request):
  posts = Post.objects
  # admin 페이지에서 확인했던 blog 안의 data
  posts_list = Post.objects.all()
      # [pagination] 블로그 모든 글들을 대상으로
  paginator = Paginator(posts_list,3)
      # [pagination] 블로그 객체 세 개를 한 페이지로 자르기
  page = request.GET.get('page')
      # [pagination] request 페이지를 변수에 넣고, request된 페이지가 뭔지 알아내면
      # [pagination] page를 key값으로 가지는 객체의 val 가져오는 작업임
  post_num = paginator.get_page(page)
      # [pagination] request된 페이지를 얻어온 후 return
  return render(request, 'home.html', {'posts':posts, 'post':post_num})
  # 명명작업: 변수 posts를 template에서 쓸 때 posts라는 이름으로 가져온다 (이름 지정할때 주의하기)
      # [pagination]: 'post':posts_num 추가
      # 여기에서 지정한 변수를 home.html에서 템플릿언어로 사용하므로 잘 기억해야함. (페이지 넘기거나 등등)

def detail(request, post_id):
  post_detail = get_object_or_404(Post, pk=post_id)
  return render(request, 'detail.html', {'post':post_detail})

    # get_object_or_404 : object가 있으면 가져오고 없으면 404 에러 띄우는 함수
      # 안에 model명과 (대문자로 시작) 불러올 게시글의 id값을 적는다. id가 pk가 됨
      # pk는 고유값이며 중복될 수 없음
    # 이렇게 담긴 데이터를 post로 넘김
    
    # 선언된 detail 함수는 request와 post_id를 함께 받아 데이터 전송
    # -> urls.py에서 인자를 전송하면
    # -> views.py에서 받아 처리

def new(request):
    return render(request, 'new.html')
  
  # create 함수 만들기
def create(request):
  post = Post()
  post.title = request.GET['title']
  # request.GET['title'] = new.heml의 form 태그 안에 있던거
  post.body = request.GET['body']
  # 여기도 마찬가지
  post.pub_date = timezone.datetime.now()
  # 입력한 시간이 자동으로 넘어가게. timezone 패키지 사용함
  post.save()
  return redirect('/' + str(post.id))
  # redirect: 요청을 처리하고 보여주는 페이지.
  # render가 요청이 들어올 때 html을 보여준다면 redirect는 url로 연결

  # 이제 DB에 데이터 저장 가능

def delete(request, post_id):
  post_num = get_object_or_404(Post, pk=post_id)
  post_num.delete()
  return redirect('/')
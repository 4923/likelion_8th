from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from faker import Faker # create10
from django.utils import timezone
from .forms import PostForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def home(request):
  posts = Post.objects
  return render(request, 'home.html', {'posts':posts})

def create10(request):
  ifake = Faker()
  for i in range(10):
    post = Post()
    post.title = ifake.name()
    post.body = ifake.sentence()
    post.pub_date = timezone.datetime.now()
    post.save()
  return redirect('/')

def details(request, post_id):
  post_detail = get_object_or_404(Post, pk=post_id)
  return render(request, 'detail.html', {'post':post_detail})


# 비어있는 폼 불러오는 내용
# def new(request):
#   form = PostForm()
#   # 새 Post form 추가하기 위해 PostForm() 함수를 호출 -> template에 넘김
#   return render(request, 'new.html', {'form': form})

# request.POST => 우리가 입력했던 데이터들이 있음
# POST == POST(ing)
def new(request):
  if request.method == "POST":
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      post = form.save(commit=False)
      post.pub_date = timezone.now()
      post.save()
      return redirect('/' + str(post.id))
  else:
    form = PostForm()
    return render(request, 'new.html', {'form': form})

# Edit
def edit(request, post_id):
  # 현재 게시글의 정보를 받아옴
  post = get_object_or_404(Post, pk=post_id)
  # 요청된 방식이 POST인지 확인
  if request.method == "POST":
      form = PostForm(request.POST, request.FILES, instance=post)
      if form.is_valid():
          post = form.save(commit=False)
          post.pub_date = timezone.now()
          post.save()
          return redirect('/' + str(post.id))
  else:
      form = PostForm(instance=post)
  return render(request, 'new.html', {'form': form})

# Delete
def delete(request, post_id):
  post = get_object_or_404(Post, pk=post_id)
  post.delete()
  return redirect('/')

def comments_create(request, post_id):
  # 댓글 달 게시글에 대한 정보
  post = Post.objects.get(pk=post_id)
  # form 태그에서 넘어온 댓글 내용
  content = request.POST.get('content')

  # 댓글 생성, 저장
  comment = Comment(post=post, content= content)  # import Comment 해야 함
  comment.save()

  # 댓글 생성 후 디테일 페이지로 redirect
  return redirect('/'+str(post_id))

# 댓글 지우기
def comments_delete(request, post_id, comment_id):
  comment = Comment.objects.get(pk=comment_id)
  comment.delete()
  return redirect('/'+str(post_id))

# 댓글 수정하기
def comments_update(request, post_id, comment_id):
  post = get_object_or_404(Post, pk=post_id)
  comment = get_object_or_404(Comment, id=comment_id)

  if request.method == 'POST':
      comment.content = request.POST.get('content')
      comment.save()
      return redirect('/'+str(post_id))

  else:
      return render(request, 'comments_update.html', {'post':post, 'comment':comment})
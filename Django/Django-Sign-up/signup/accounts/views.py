from django.shortcuts import render, redirect
from django.contrib.auth.models import User # User Model 연결
from django.contrib import auth # login page 구현 위해 auth import

# SMTP 관련 인증
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token

# views.py: url 제어

def home(request):
  return render(request, 'home.html')

def signup(request):
  # request가 POST method일때
  if request.method == 'POST':
    # 입력받는 password 1과  password2가 같으면
    if request.POST['password1'] == request.POST['password2']:
      # ------ 0917 SMTP ------
      # 회원 생성 후
      user = User.objects.create_user(username=request.POST['username'], email=request.POST["email"], password=request.POST['password1'])
      # 유저 비활성화 (인증이 안됐으므로)
      user.is_active = False
      user.save()
      current_site = get_current_site(request)
      message = render_to_string('activation_email.html',{
        'user':user,
        'domain':current_site.domain,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token':account_activation_token.make_token(user),
      })
      mail_title = "계정 활성화 확인 이메일"
      mail_to = request.POST["email"]
      email = EmailMessage(mail_title, message, to=[mail_to])
      email.send()
      return render(request, 'home.html', { 'error': 'Please check your account activation email'})
      # ------ ------ ------
      
      # home.html로 돌아감
      # return redirect ('home')
  # password가 서로 같지 않을 땐 다시 signup.html return
  return render(request, 'signup.html')

def login(request):
  # request가 POST method일때
  if request.method == 'POST':
    # DB check: 입력받는 ID, PW가 존재하는지
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(request, username=username, password=password)
    # 유저가 있다면
    # if user != '': 이렇게 하면 input 값이 공백인지 아닌지를 판단하는거니까 다 home.html로 연결됨
    # != 쓰고싶으면 != None
    if user != None:
      # 로그인하고 home으로 redirect
      auth.login(request, user)
      return redirect('home')
    # 유저가 없다면
    else:
      # 에러를 표시, login 페이지로 새로고침
      return render(request, 'login.html', {'error': 'username or password is incorrect.'})
  # POST 요청이 아닐 경우 login 페이지 새로고침
  return render(request, 'login.html')

def logout(request):
  # 로그아웃 하면 home으로 redirect
  auth.logout(request)
  return redirect('home')

def userpage(request):
  # 로그인 했을경우 해당 페이지 접속 허가
  if request.user.is_authenticated:
    return render(request, 'userpage.html')
  # 아닐경우 index로 돌아가기
  else:
    return render(request, 'home.html', { 'error': 'Only site member can accesss userpage'})
    # return render(request, 'userpage.html', {'error' : 'Only site member can access userpage'})

# 계정 활성화 함수 (토큰을 통해 인증)
def activate(request, uidb64, token):
  try:
      uid = force_text(urlsafe_base64_decode(uidb64))
      user = User.objects.get(pk=uid)
  except(TypeError, ValueError, OverflowError, User.DoesNotExsit):
      user = None
  if user is not None and account_activation_token.check_token(user, token):
      user.is_active = True
      user.save()
      auth.login(request, user)
      return render(request, 'home.html', { 'error': 'Your Accounts is activate'})
  else:
      return render(request, 'home.html', { 'error': '계정 활성화 오류'})
  return 
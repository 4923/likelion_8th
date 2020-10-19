from django.db import models

# Create your models here.

# 1:N 관계 설정 (Databare Relation)
# Post Class
class Post(models.Model):
  # 최대 200글자 title field 생성
  title = models.CharField(max_length=200)
  # image는 images/라는 경로에 업로드되고 이미지는 없어도 상관 없음 (blank=True)?
  image = models.ImageField(upload_to='images/', null=True, blank=True)
  # 생성시간
  pub_date = models.DateTimeField('date published')
  # 본문
  body = models.TextField()

  # 제목 -> 제목
  def __str__(self):
    return self.title
  
  # 본문 요약 (20글자까지)
  def summary(self):
    return self.body[:20]

# Comment class
# post는 models.ForeignKey() 객체가 저장되어있는 변수
class Comment(models.Model):
  # Django에서 모델을 구현할 때 ForeignKeyField를 자주 사용하는데 DB의 '참조 무결성'을 유지하기 위해 ForeignKeyField가 바라보는 값이 삭제될 때 어떻게 처리할지 미리 옵션으로 설정.
    # CASCADE: ForeignKey(ondelete='~~~') 종류가 많은데 CASCADE는 ForeignKeyField가 바라보는(지정하는??) 값이 삭제될 때 모델 인스턴스(row)도 함께 삭제
    # PROTECT:삭제되지 않도록 ProtectedError를 발생
    # SET_NULL: 값이 삭제될 때 ForeignKeyField값을 null로 변경 (null=True일 때만 가능)
    # SET_DEFUALT: SET_NULL이 ForeignKeyField값을 null로 바꾼다면 SET_DEFAULT는 default로 변경. (default값이 있을때만 가능)
    # SET(): ForeignKeyField값이 삭제될 때 해당 값을 Set에 설정한 함수에 의해 설정한다
    # DO_NOTHING: 삭제될 때 아무런 행동을 취하지 않는다. **참조무결성을 해칠 위험이 있다.**
  post = models.ForeignKey('myblog.Post', on_delete=models.CASCADE)
  content = models.TextField()

  def __str__(self):
    return self.content
<h1 aligns="center"> ForeignKeyField </h1>

[TOC]

<h3 aligns="center"> 1. 1:N관계 설정 </h3>
게시글에 댓글을 쓸 때 한 게시글에 여러개의 댓글이 달리므로 게시글과 댓글은 1:N구조를 띔 (1:다)

<h3 aligns="center">
  2. ForeignKeyField <a href="https://lee-seul.github.io/django/backend/2018/01/28/django-model-on-delete.html">참고</a>
</h3>

`post = models.ForeignKey('myblog.Post', on_delete=models.CASCADE)`

오늘 작성한 `models.py/Class/Comment`에서
* `post`는 `models.ForeignKey()`를 객체로 가지는 변수. </ul>
> 댓글(Comment)이 새로 생성될때, 어떠한 게시글(Post)인지를 나타내는 대한 변수 명입니다.


* `models.ForeignKey()`는 외래키를 설정하는 함수.
인자를 각각 설명하면
* 첫번째인자: ForeignKey()가 연결되는 테이블. 여기서는 `'myblog.Post'`이므로 models.py에서 정의한 Post Class를 의미함.
* 두번째 인자: ForeignKeyField가 삭제될 때 어떻게 처리할지


* **CASCADE**: 자기자신도 삭제
(게시글이 삭제되면 댓글도 삭제)
* **PROTECT**: 하위값이 존재하면 상위값 삭제 불가 -> `ProtectedError`발생
(게시글이 존재하면 댓글 삭제 불가)
* **SET_NULL**: 상위값이 삭제되면 하위값은 그대로 두되 하위값의 상위정보를 NULL로 변경
(게시글이 삭제되면 댓글의 게시글 정보를 NULL로 변경)
* **SET_DEFUALT**: SET_NULL이 ForeignKeyField값을 null로 바꾼다면 SET_DEFAULT는 default로 변경. (default값이 있을때만 가능)
(게시글이 삭제되면 댓글의 게시글 정보를 default 값으로 변경)
* **SET()**: ForeignKeyField값이 삭제될 때 해당 값을 Set에 설정한 함수에 의해 설정한다
* **DO_NOTHING**: 삭제될 때 아무런 행동을 취하지 않는다. **참조무결성을 해칠 위험이 있다.**

<h3 aligns="center">
  1. 무결성 Integrity <a href="https://untitledtblog.tistory.com/123">[참고]</a>
</h3>
DB에서 지정된 값들에 여러가지 연산 제한을 걸어 신뢰를 보장하게 하는 데이터베이스 관리시스템(DBMS)의 기능
* 데이터의 정확성, 일관성, 유효성을 유지하게한다.

<h4> 무결성의 종류에는 </h4>

**1. 개체 무결성 Entity Integrity**
모든 데이터들이 기본키 Primary Key로 선택된 필드 column을 가진다. 모두 고유값을 가져야하며 빈 값은 허용되지 않는다.<br>
-> 모든 개체가 PK로 선택된 필드를 가지고 있는가<br>

**2. 참조 무결성 Referential Integrity**
관계형 DB Model에서 (1:1, 1:N, N:N) 참조관계에 있는 두 테이블의 데이터가 항상 일관된 값을 유지하고 있는지 확인.<br>
* 지워져서 존재하지 않는 게시글의 댓글등을 관리할 수 있다.<br>
-> Foreign Key를 활용.<br>
**3. 도메인 무결성 Domain Integrity**
테이블에 존재하는 필드의 무결성을 보장. 필드의 타입, Null 값의 허용 등을 정의하고 올바른 데이터가 입력되었는지 확인<br>
* 예) 주민등록번호 필드에 알파벳이 입력된 경우<br>
**4. 무결성 규칙 Integrity Rule**
DB에 공통적으로 적용되는 규칙. DB를 사용하는 유저에 따라 다르게 적용되는 비즈니스 규칙 business rule과는 다르게 무결성 규칙은 DB에 공통으로 적용된다<br>


<h4> 키의 종류와 기능 </h4>

**1. 슈퍼 키 Super Key**<br>
* 테이블에 존재하는 필드의 부분집합.
* 유일성 uniqueness을 만족: 다른 값과 구별되는 유일한 값이어야한다. 중복되는 값이 없어야함.
  
**2. 후보 키 Candidate Key**<br>
* 기본키 PK가 될 수 있는 후보.
* 유일성과 최소성irreducibility을 만족해야함.
* 최소성: 최소한의 필드로 레코드를 유일하게 구별할 수 있어야 함

**3. 기본 키 Primary Key**<br>
* 후보 키 중에서 선택된 고유한 식별자
* 유일성, 최소성을 만족해야하며 Null을 가질 수 없음
* 적절한 PK란?
  + 자주 변경되지 않는 값
  + 단순한 값

**4. 대체 키 Alternate Key**<br>
기본키로 선택되지 않은 후보키들. 후보키 - 기본키

**5. 복합 키 Composite Key**<br>
한 개 이상의 필드를 포함하는 키

**6. 외래 키 Foreign Key**<br>
* 다른 테이블의 레코드를 식별할 수 있는 키. 참조하기 위해 사용된다.
* 참조관계에 있는 테이블 사이에선 참조무결성 문제가 발생할 수 있다. 이를 해결하기 위해 `models.ForeignKey()`의 두번째 인자를 사용한다.

* 외래키의 속성
  + 하나의 필드 또는 전체 필드의 부분집합으로 구성
  + 중복된 값과 Null 가질 수 있다.
  + 반드시 **참조되는 테이블**에서 **유일성**을 만족하는 필드를 참조해야한다. -> PK를 참조할 수 도 있다.
  + 참조되는 테이블에 **존재하는 값**만을 가져야 한다. 단, Null은 예외
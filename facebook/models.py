from django.db import models

# Create your models here.

'''
이 파일은 저희가 데이터베이스에 저장하거나 서버에서 사용하게 될
객체 변수 박스를 정의하는 곳입니다. class와 object의 개념에 대해 설명드렸는데,
class와 object의 개념이 이해가 되지 않으신 분은 드린 교재나 구글 검색으로
class와 object의 개념을 한 번 보고 오신 후 주석을 읽으시면 더 쉽게 이해할 수 있습니다.

여기서는 상속의 개념도 들어가 있는데, 상속의 개념도 설명드렸습니다.
(갤럭시와 아이폰은 핸드폰이라는 class를 상속한다는 개념)
이 부분이 이해가 되지 않으시면, 검색하셔도 좋고 깊이 생각하지 않으셔도 좋습니다.
(models.Model) 부분이 상속을 명시한 부분입니다.

서버에서 사용하게 될 class 박스의 이름과 그 안에 어떤 내용물들이 들어가고,
그 내용물들은 어떤 자료형을 가지고 있는지 정의하는 부분입니다.

상속의 개념이 들어가기 때문에 __str__ 부분의 왼쪽 줄 부분의 파란 동그라미 부분에
마우스를 올리시면 override라고 써있는데, 상속을 이해하실 수 있는 분들은
아~ 오버라이드구나~ 하고 넘어가시고, 모르시는 분들도 아 동그라미가 있구나~ 하고
넘어가셔도 괜찮습니다. 
'''

class Article(models.Model):
    author = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    text = models.TextField()
    password = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Page(models.Model):
    master = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# 6주차
# 코멘트 모델
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')  #외래키 (외부 모델의 pk와 관계를 알려줌)
    #CASCADE 선언으로 코멘트가 게시글에 종속됨을 선언
    author = models.CharField(max_length=120)
    text = models.TextField()
    password = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


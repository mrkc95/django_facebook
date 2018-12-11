"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
'''
urls.py는 저희가 만드는 웹 애플리케이션이 요청을 받을 때
요청에 대한 경로에 대해 어떤 동작을 할지 명시해주는 설정이 들어가는 파일입니다.

저희가 기본적으로 서버(에서 동작하고 있는 웹 애플리케이션)에 요청을 줄 때,
브라우저에서 원하는 페이지를 보기 위해 브라우저 상단에 주소를 입력하죠?
예 : https://comic.naver.com/webtoon/weekday.nhn (네이버 웹툰 접속 주소)

예시로 써놓은 페이지 주소를 분석하자면
https://   -> 프로토콜(규약)을 명시하는 부분입니다. 여러분들이 가장 많이 본게
                http나 https가 있는데 웹페이지를 보기 위해 정해놓은 데이터들의
                규칙이라고 생각하시면 됩니다. 브라우저는 기본적으로 둘 중 하나의
                규칙을 사용해서 서버에 데이터(페이지 자료)를 요청하게 됩니다.
                (https 에서 s는 SSL, Secure등의 보안을 강화한 http와 똑같은 규칙입니다.
                
comic.naver.com -> 저희가 pycharm을 이용해서 run을 누르게 되면
                    여러분들의 컴퓨터를 서버로 이용해서 웹 애플리케이션이 동작하게 되고,
                    그 애플리케이션은 127.0.0.1 의 주소를 할당받게 됩니다.(로컬, 나 자신을 가리키는 IP주소)
                    저희가 만드는 프로그램이 뜨는 컴퓨터의 주소를 포함하여 모든 네트워크 상의
                    컴퓨터는 각 고유의 IP주소를 할당받아 자신의 위치를 나타내는데,
                    23.53.253.58 이런식으로 숫자를 외우기는 귀찮아서
                    특정 문자열에 IP 주소를 맵핑한 DNS서버라는게 네트워크 상에 존재합니다.
                    DNS서버는 문자열을 IP주소로 변환해주는 역할을 하고 있는데,
                    
                    예시 주소가 DNS서버로 들어가게 되면
                    https://comic.naver.com/webtoon/weekday.nhn
                ->  https://23.53.253.58/webtoon/weekday.nhn
                    
                    이런 식으로 변환이 되서 어느 서버에 요청을 보내게 될지 알 수 있게 되는거죠.
                    실습때 pycharm으로 띄우는 저희의 프로그램은 127.0.0.1:8000이라고 끝에
                    포트번호까지 명시가 되어 있는데, 포트번호를 생략하면
                    브라우저가 자동으로 80번 포트로 요청을 보내게 됩니다.
                    
                    포트는 쉽게 생각해서
                    IP주소가 아파트 주소면 포트번호는 몇 동 몇 호인지 찾아갈 수 있게 하는
                    번호라고 생각하시면 됩니다.
                    이 부분을 통틀어서 host라고 표현합니다.
                    
/webtoon/weekday.nhn -> 이 부분이 이제 path(경로)가 되고,
                        저희가 urls.py에 명시해서 어떤 경로로 들어오게 되면
                        어떤 동작을 할지 결정하게 되죠.
                        예시는 /webtoon/weekday.nhn 이 경로로 요청했지만
                        저희가 실습할 때는 /play, /newsfeed 등의 경로를 설정했었죠?
                        경로에 대한 설정을 여기 urls.py의
                        urlpatterns 라는 배열(array) 안에 넣어놓게 되면,
                        프로그램이 동작할 때 이 파일을 찾아와서 어떤 경로로 들어왔을 때
                        어떤 동작을 할지 알아간 후, 요청에 맞게 행동하기 위해
                        기다리게 됩니다.
                    
                    

'''

'''
import 부분입니다. 스터디 시간에 설명드렸듯이 import구문은
다른 파일에 정의되어 있는 변수나 함수를 이 파일에서도 가져다 쓰기 위해서
선언해놓는 구문입니다.

예시 : from facebook.views import play
뜻 : facebook 안의 views라는 파일에서 play라는 친구를 가져다가
     urls.py 안에서도 쓰겠다!
     
     이 때, play는 변수가 될 수도 있는거고 함수가 될 수도 있고
     여기서는 views.py 안에 정의되어 있는 play함수를 가져다 쓰겠다는 의미입니다.
'''
from django.contrib import admin
from django.urls import path
from facebook.views import play
from facebook.views import play2
from facebook.views import newsfeed
from facebook.views import detail_feed
from facebook.views import new_feed
from facebook.views import remove_feed, edit_feed

'''
urlpatterns 라는 이름의 변수 박스가 배열 형태로 들어있습니다.
이 안의 각 요소들을 이용해서 django가 경로에 따라 어떤 행동을 하게 될지
알게 되는데, 자세히 보면 모양이 전부 path(문자열, 함수이름)으로 쓰여져 있죠?

path() 이렇게 소괄호가 이름 뒤에 쳐져 있으면 함수 호출 구문입니다.
함수는 소괄호 안의 전달인자를 받아서 정의되어 있는 연산을 수행한 후
결과물을 되돌려주는(return) 역할을 한다고 설명드렸는데,
함수 호출 구문이 배열의 각 요소로 있다는 얘기는 실질적으로
path() 함수의 호출 결과가 배열의 요소로 저장된다는 의미입니다.
(이 부분이 이해가 안되시면 간단하게 경로 맵핑이 저장된다고 생각하시면 됩니다.)

detail_feed를 맵핑한 부분을 보시면 <pk> 이렇게 꺽새 괄호가 있는 부분이 있는데 
맵핑 정보 중에 feed/<pk>/ 이 부분은
<pk> 여기에 써져있는 문자열을 detail_feed라는 함수의 전달인자로 넘기겠다는 뜻입니다.
views.py에 정의되어 있는 detail_feed 함수를 보시면 전달인자로
request, pk 를 가지고 있죠? 여기의 pk에다가 경로에서 전달받은 값을 넣고
detail_feed 함수를 실행하게 되는거죠.
예로 feed/1/ 을 넣으면 pk가 1이 되는거고, feed/asd/ 라고 쓰면 pk에 asd라는 값이
들어가게 됩니다.
'''
urlpatterns = [
    path('admin/', admin.site.urls),

    path('play/', play),

    path('play2/', play2),

    path('', newsfeed),
#4주차
    path('feed/<pk>/', detail_feed),  # primary key(주키, 완전 독립적으로 구분 가능한 key) RDB(관계형 DB)

#5주차
    path('new/', new_feed),

    path('feed/<pk>/remove/', remove_feed),

    path('feed/<pk>/edit/', edit_feed),
#6주차
]
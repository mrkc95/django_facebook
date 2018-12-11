from django.shortcuts import render, redirect
from facebook.models import Article
from facebook.models import Comment

# Create your views here.
'''
이 파일은 함수가 정의되어 있거나 view(보여줄) 내용을 정의하는 파일로,
함수를 통해서 저희가 원하는 작업(계산이나 데이터베이스 접근 등)을 수행한 후,
사용자에게 어떤 결과를 보내주게 될지 정의하게 되는 파일입니다.
저희가 작성한 방식은 전부 함수를 활용하고 있는데, 함수의 개념이
이해가 잘 안되시는 분은 제가 드린 교재의 함수 부분을 천천히 읽어보시고
다시 보시면 더 이해가 잘 됩니다!
'''

def play(request):
    return render(request, 'play.html')


count = 0


def play2(request):
    choidogeun = '최도근'
    age = 20
    global count  # 바깥영역의 변수를 사용할 때 global
    count = count + 1  # 접속할 때마다 방문자 1 증가

    if age > 19:
        status = '성인'
    else:
        status = '청소년'

    return render(request, 'play2.html', {'name': choidogeun, 'cnt': count, 'age': status})


def newsfeed(request):
    articles = Article.objects.all()

    return render(request, 'newsfeed.html', {'articles': articles})


def detail_feed(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':  # 댓글 등록 시 댓글 저장 후 redirect
        Comment.objects.create(
            article=article,
            author=request.POST.get('nickname'),
            text=request.POST.get('reply'),
            password=request.POST.get('password')
        )

        return redirect(f'/feed/{article.pk}')

    return render(request, 'detail_feed.html', {'feed': article})
# author = ???
# title = ??
# comments = ????



# 5주차
'''
new나 edit, remove는 모두 비슷한 액션을 하기 때문에 new_feed 기준으로
주석으로 설명드리겠습니다.
'''
def new_feed(request):
    ''''''
    '''
    분기문이 2개가 있는데
    분기문의 첫 번째 조건은 요청 방식이 POST일때만 아래 구문이 실행하게 되어 있습니다.
    브라우저를 통해 웹 요청을 보내는 방식이 크게 GET, POST가 있다고 말씀드렸는데
    (5주차 때 못나오신 분들은 구글에 GET POST 방식이라고 검색하시면 자세히 나옵니다.)
    지금은 POST방식일 때만 if문 안에 들어있는 코드를 실행하게 되고,
    GET방식으로 오게 될 경우(브라우저에 /new 주소를 입력해서 들어오게 될 경우)
    if문 안의 있는 코드들이 실행되지 않고
    return render(request, 'new_feed.html') 이 코드를 바로 실행하게 됩니다.
    '''
    if request.method == 'POST': # 폼이 전송되었을 때만 아래 코드를 실행
        '''
        또 if문이 나왔는데, 이 경우는 요청에 들어있는 4개의 값들 중 전부가
        빈 문자열이 아닐 경우에 아래 코드를 실행하게 되고 하나라도 빈 값이 나오게 되면
        GET 방식의 요청이 온 것과 동일하게
        return render(request, 'new_feed.html')을 실행하게 됩니다.
        '''
        if request.POST['author'] != '' and request.POST['title'] != '' and request.POST['content'] != '' and request.POST['password'] != '':
            '''
            new_article이라는 이름의 변수 박스를 하나 만드는데 그 박스는
            Article.objects.create() 라는 함수를 호출해서 받은 결과물로
            채우고 있습니다.
            Article 안의 obejcts 안의 create라는 함수는 밑에 코드를 보시면
            comma로 구분되어 4개의 전달인자를 받고 있도록 써있죠?
            각 전달인자들은 request.POST[문자열] 의 값을 대입받아서 채워지게 되는데,
            request.POST[문자열] 은 POST요청에서 body 안에 (폼 안에) 들어있는 정보들에서
            문자열과 일치하는 키 값의 내용을 가져옵니다.
            (POST 요청의 내용물을 까보면 key=value&key=value&key=value... 이런식으로
            서버에 값을 전달하고 있는데, author=aa&title=bb 이런식으로 요청이 오면
            request.POST['author'] 의 값은 aa가 되는거죠. 
            '''
            new_article = Article.objects.create(
                author=request.POST['author'],
                title=request.POST['title'],
                text=request.POST['content'],
                password=request.POST['password']
            )
            '''
            Article.objects.create라는 함수의 내용 안에는
            데이터베이스에 전달인자로 받은 값들을 하나의 Article로 만들어
            저장하게 됩니다. 여기까지 오면 데이터베이스에도 폼에서 받은 정보들로
            만든 Article이 하나 들어가있고, new_article이라는 변수 박스에도
            똑같은 내용의 Article이 하나 들어가있는 모양이 됩니다.
            
            그리고 최종적으로 밑에 기존에 보던 render가 아닌 redirect 함수를 불러서
            사용자에게 결과를 되돌려주고 있죠? redirect는
            서버가 스스로 사용자가 웹브라우저에 주소를 입력한 것과 똑같은
            행동을 대신 해주는 기능입니다. 좀 더 자세히 알고 싶으신 분들은
            구글에 'URL 리다이렉트'라고 검색하면 알 수 있습니다.
            저희가 urls.py에 /feed/<pk>/ 경로를 detail_feed로 맵핑해놨었죠?
            거기로 서버가 대신 요청을 한 번 더 전달하게 됩니다.
            
            문자열 앞에 f가 붙어있는 걸 볼 수 있는데,
            f가 문자열 앞에 붙으면 문자열 안의  {  } 중괄호의 내용을
            문자열이 아닌 변수 박스 안의 내용물을 까서 내용을 대체하게 됩니다.
            f가 붙지 않으면 저 함수는 feed/<pk>/ 의 pk 안에다가
            '{new_article.pk}' 라는 값을 넣어서 보내게 되버립니다.
            f를 붙이면 저희가 방금 만든 변수 박스 new_article 안의 pk라는 값을
            저기다가 대신 넣게 되는거죠. 방금 만든 박스의 pk라는 값이 3이면
            리다이렉트 경로가 /feed/3/ 이렇게 완성되서 보내지게 됩니다.
            여기 과정까지 이해가 되셨으면, remove와 edit도 똑같은 원리이기 때문에
            주석없이 읽어보시고 이해해보시면 됩니다!
            '''

            # 새글 등록 끝
            return redirect(f'/feed/{ new_article.pk }')

    return render(request, 'new_feed.html')


def remove_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.delete()
            return redirect('/') # 첫페이지로 이동하기

    return render(request, 'remove_feed.html', {'feed': article})


def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        article.author = request.POST['author']
        article.title = request.POST['title']
        article.text = request.POST['content']
        article.save()
        return redirect(f'/feed/{ article.pk }')

    return render(request, 'edit_feed.html', {'feed': article})
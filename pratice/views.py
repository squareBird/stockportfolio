from django.shortcuts import render
# 게시글(Post) 활용을 위해 import
from .models import Post

def index(request):
    return render(request, 'pratice/index.html')

# 게시글 목록
def blog(request):
    # postList에 현재 Post 객체에 들어있는 값 모두 가져오기
    postList = Post.objects.all()
    return render(request, 'pratice/blog.html', {'postList':postList})

# blog의 게시글을 부르는 posting 함수(pk 즉 기본키를 이용해 조회)
# 현재 동작순서
# 1. blog.html에서 a herf="현재url/Post pk"로 url 접속을 시켜줌
# 2. urls.py에서 posting 함수 동작
# 3. views.py의 posting 함수 동작
# 4. 여기서 궁금한게 posting의 pk는 누가 보내주는걸까?
# 5. urls.py에 보면 <int:pk>라고 되어있다 여기서 보내준다.
def posting(request, pk):
    post = Post.objects.get(pk=pk)
    # return render(request, 'pratice/posting.html', {'post':post})
    return render(request, 'pratice/posting.html', {'post':post, 'test':'text'})
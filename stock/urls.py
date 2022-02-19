from django.urls import path
from . import views

app_name='pratice'

urlpatterns = [
    path('', views.index, name='index'),
    # URL:80/blog에 접속하면 blog 페이지 + URL이름은 blog
    path('blog/', views.blog, name='blog'),
    # URL:80/blog/숫자로 접속하면 게시글-세부페이지(posting)
    # path('blog/<int:pk>', views.posting, name='posting'),
    # 위에처럼도 되고 아니면 밑에처럼 <int:pk>뒤에 특정 문자열 입력하게 제한도 가능
    path('blog/<int:pk>/result', views.posting, name='posting'),
]
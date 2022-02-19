from django.db import models

# Create your models here.

# 모델 생성 후
# 1. python manage.py makemigrations
# 2. python manage.py migrate

# 모델 변경시
# 1. app의 migrations폴더 안에 _init_.py 빼고 전부 제거
# 2. db에서 [model명]_post(?) 테이블 드롭
# 3. python manage.py showmigrations
# 4. python manage.py migrate --fake [마이그레이션명] zero

class Post(models.Model):
    postname = models.CharField(max_length=50)
    contents = models.TextField()

    # admin 페이지의 게시글 제목 바꾸기
    def __str__(self):
        return self.postname


# class Post2(models.Model):
#     title = models.CharField(max_length=255)
#     slug = models.SlugField(unique=True, max_length=255)
#     description = models.CharField(max_length=255)
#     content = models.TextField()
#     published = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ['-created']
from django.contrib import admin
from .models import Post

# Register your models here.

# python manage.py createsuperuser 통해 admin 슈퍼계정을 만들어주저야 함

admin.site.register(Post)
# admin.site.register(Post2)
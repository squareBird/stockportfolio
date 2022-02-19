from django.db import models

# Create your models here.

# 포트폴리오 사용자
class User(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)

class Stock(models.Model):

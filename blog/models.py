import uuid

from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
#モデル作成の場所
#ORM　ｰ>　テーブルとオブジェクトを1：1で結ぶ機能
User= get_user_model()

class Post(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  title = models.CharField(max_length=200)
  content = models.TextField(max_length=5000)
  header_image = models.ImageField(upload_to="images/", null=True, blank= True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  auther = models.ForeignKey(
    User,
    on_delete = models.CASCADE
  )
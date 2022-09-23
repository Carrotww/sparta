#user/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserModel(AbstractUser): # 적용하기 위해서 admin.py에서 적용 시켜주어야 함
    class Meta:
        db_table = "my_user"
        # 테이블 이름을 나타냄

    bio = models.CharField(max_length=256, default='')
    # user model을 가져왔고 bio 만 추가해서 사용
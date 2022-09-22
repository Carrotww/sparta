#user/models.py
from django.db import models


# Create your models here.
class UserModel(models.Model): # 적용하기 위해서 admin.py에서 적용 시켜주어야 함
    class Meta:
        db_table = "my_user"
        # 테이블 이름을 나타냄

    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=256, null=False)
    bio = models.CharField(max_length=256, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
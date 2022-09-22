from django.contrib import admin
# django에서 admin 툴을 사용하겠다
from .models import UserModel
# 생성한 python file을 불러옴

# Register your models here.
admin.site.register(UserModel) # 이 코드가 나의 UserModel을 Admin에 추가 해 줍니다
# 가져온 것을 관리자 페이지에 넣어주겠다 라는 것
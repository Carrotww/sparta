from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model # 사용자가 데이터베이스 안에 있는지 검사하는 함수
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        # username 변수에 post로 가져온 데이터 중에서 'username' 해당하는 데이터를 가져 오겠다 없으면 None
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        bio = request.POST.get('bio', None)

        if password != password2:
            return render(request, 'user/signup.html')
        else:
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html')
            else:
                UserModel.objects.create_user(username=username, password=password, bio=bio)
                return redirect('/sign-in')

def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = auth.authenticate(request, username=username, password=password)
        # password를 암호화 했기 때문에 그냥 == 으로 비교하는 것이 아닌 복호화 해서 비교해야함 Django기능
        # me = UserModel.objects.get(username=username)
        # if me.password == password:
        if me is not None: # me에서 모든 기록을 들고 오기 때문에 있는지 없는지만 비교를 하면 됨
            # request.session['user'] = me.username
            auth.login(request, me)
            return redirect('/') # / 라는 기본 페이지로 감 -> tweet.app에 '' 가 기본 url
        else:
            return redirect('/sign-in')

    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signin.html')

@login_required # 사용자가 로그인이 되어있어야만 접근 가능한 함수
def logout(request):
    auth.logout(request)

    return redirect('/')
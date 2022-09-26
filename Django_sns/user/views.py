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
        username = request.POST.get('username', '')
        # username 변수에 post로 가져온 데이터 중에서 'username' 해당하는 데이터를 가져 오겠다 없으면 
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        bio = request.POST.get('bio', '')

        if password != password2:
            return render(request, 'user/signup.html', {'error':'패스워드를 확인 해 주세요!'})
        else:
            if username == '' or password == '':
                return render(request, 'user/signup.html', {'error':'사용자 이름과 비밀번호를 입력해 주세요.'})

            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html', {'error': '사용자가 존재합니다.'})
            else:
                UserModel.objects.create_user(username=username, password=password, bio=bio)
                return redirect('/sign-in')

def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        me = auth.authenticate(request, username=username, password=password)
        # password를 암호화 했기 때문에 그냥 == 으로 비교하는 것이 아닌 복호화 해서 비교해야함 Django기능
        # me = UserModel.objects.get(username=username)
        # if me.password == password:
        if me is not None: # me에서 모든 기록을 들고 오기 때문에 있는지 없는지만 비교를 하면 됨
            # request.session['user'] = me.username
            auth.login(request, me)
            return redirect('/') # / 라는 기본 페이지로 감 -> tweet.app에 '' 가 기본 url
        else:
            return render(request, 'user/signin.html', {'error':'이름 혹은 패스워드를 확인 해 주세요'})

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


@login_required
def user_view(request):
    if request.method == 'GET':
        # 사용자를 불러오기, exclude와 request.user.username 를 사용해서 '로그인 한 사용자'를 제외하기
        user_list = UserModel.objects.all().exclude(username=request.user.username)
        # 친구 list 사용자 list를 볼 예정이라 exclude로 자신을 제외한 사용자 정보를 가져온다
        return render(request, 'user/user_list.html', {'user_list': user_list})


@login_required
def user_follow(request, id):
    me = request.user
    click_user = UserModel.objects.get(id=id)
    # click_user -> 팔로우 버튼을 눌린 사용자
    if me in click_user.followee.all():
        # 팔로우 하려는 사람의 팔로워를 모두 가져와서 내가 있으면
        click_user.followee.remove(request.user)
        # 팔로위 취소를 해줌
    else:
        click_user.followee.add(request.user)
        # 팔로워중에 내가 없다면 나를 추가해준다
    return redirect('/user')
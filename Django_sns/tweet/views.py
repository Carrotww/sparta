from django.shortcuts import render, redirect

def home(request):
    user = request.user.is_authenticated
    # user가 login 되어있는지 안 되어 있는지 확인할 수 있음 Django 기본 기능
    if user:
        return redirect('/tweet')
    else:
        return redirect('/sign-in')

def tweet(request):
    if request.method == 'GET':
        return render(request, 'tweet/home.html')
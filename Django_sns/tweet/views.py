from django.shortcuts import render, redirect
from .models import TweetModel
from .models import TweetComment
from django.contrib.auth.decorators import login_required

def home(request):
    user = request.user.is_authenticated
    # user가 login 되어있는지 안 되어 있는지 확인할 수 있음 Django 기본 기능
    if user:
        return redirect('/tweet')
    else:
        return redirect('/sign-in')

def tweet(request):
    if request.method == 'GET':
        user = request.user.is_authenticated # 인증된 사용자가 있나

        if user:
            all_tweet = TweetModel.objects.all().order_by('-created_at')
            # TweetModel 에 저장된 object를 다 가져온다. -작성 순
            # order_by로 최신 순으로 불러온다
            return render(request, 'tweet/home.html', {'tweet':all_tweet})
            # dict() 형태로 key : tweet, value : all_tweet
        else:
            return redirect('/sign-in')
        
    elif request.method == 'POST':
        user = request.user # 모든 사용자 정보를 가져옴
        my_tweet = TweetModel() # 인스턴스 생성
        my_tweet.author = user # user를 넣어주고
        my_tweet.content = request.POST.get('my-content', '')
        # post로 받아온 content를 가져옴
        my_tweet.save()
        return redirect('/tweet')

@login_required
def delete_tweet(request, id):
    my_tweet = TweetModel.objects.get(id=id)
    my_tweet.delete()
    return redirect('/tweet')

@login_required
def detail_tweet(request, id):
    my_tweet = TweetModel.objects.get(id=id)
    tweet_comment = TweetComment.objects.filter(tweet_id=id).order_by('-created_at')
    return render(request,'tweet/tweet_detail.html',{'tweet':my_tweet,'comment':tweet_comment})


@login_required
def write_comment(request, id):
    if request.method == 'POST':
        comment = request.POST.get("comment","")
        current_tweet = TweetModel.objects.get(id=id)

        TC = TweetComment()
        TC.comment = comment
        TC.author = request.user
        TC.tweet = current_tweet
        TC.save()

        return redirect('/tweet/'+str(id))


@login_required
def delete_comment(request, id):
    comment = TweetComment.objects.get(id=id)
    current_tweet = comment.tweet.id
    comment.delete()
    return redirect('/tweet/'+str(current_tweet))
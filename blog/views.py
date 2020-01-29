from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.


def index(request):
    return HttpResponse('Hello World!')

def test1(request):
    return HttpResponse('Hello Yen!')

def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts,3) # 顯示 3 篇文章
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger: #若 page 不是一個整數則返回第一頁
        posts = paginator.page(1)
    except EmptyPage: #若 page 超出
        posts = paginator.page(paginator.num_pages)
    return render(request,'blog/post/list.html',{'page':page,'posts':posts})

def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post,slug=post,status="published",publish__year=year,publish__month=month,publish__day=day)
    return render(request,'blog/post/detail.html',{'post':post})
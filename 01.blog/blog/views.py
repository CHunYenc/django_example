from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailPostForm , CommentForm
from django.core.mail import send_mail


# Create your views here.


def index(request):
    return HttpResponse('Hello World!')


def test1(request):
    return HttpResponse('Hello Yen!')


def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 3)  # 顯示 3 篇文章
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:  # 若 page 不是一個整數則返回第一頁
        posts = paginator.page(1)
    except EmptyPage:  # 若 page 超出
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status="published", publish__year=year, publish__month=month,
                             publish__day=day)
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comments_form = CommentForm()
    return render(request, 'blog/post/detail.html', locals())


def post_share(request, post_id):
    # 通過 id 找到　post 對象
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == "POST":
        # 如果表單有提交
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # 表單驗證
            cd = form.cleaned_data  # 只接收通過驗證的資料　cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) test you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}"\n\n{}\'s comments:{}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'b10610020@g.chu.edu.tw', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})

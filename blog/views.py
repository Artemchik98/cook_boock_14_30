from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post, PostPoint,Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from  .forms import EmailPostForm,CommentForm
from  django.core.mail import send_mail
from taggit.models import Tag
from django.db.models import Count

def post_list(request,tag_slug=None):
    object_list=Post.objects.all()
    tag=None
    print(tag)

    if tag_slug:
        tag=get_object_or_404(Tag,
                      slug=tag_slug)
        object_list=object_list.filter(
            tags__in=[tag])
    paginator=Paginator(object_list,3)
    page=request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)



    return render(request,'blog/post/list.html',
                  {'page':page,
                   'posts':posts,
                   'tag':tag})






class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_detail(request, year, month, day, post):
    post_object = get_object_or_404(Post, slug=post,#status='published',
                                    publish__year=year,
                                    publish__month=month,
                                    publish__day=day)
    comments=post_object.comments.filter(active=True)
    new_comment=None
    post_points = PostPoint.objects.filter(
        post=post_object)

    if request.method=="POST":
        comment_form=CommentForm(data=request.POST)
        if comment_form.is_valid():
            # new_comment=comment_form.save(commit=False)
            # new_comment.post=post
            # new_comment.save()
            cd=comment_form.cleaned_data
            new_comment=Comment(post=post_object,
                                name=cd['name'],
                                email=cd['email'],
                                body=cd['body'])
            new_comment.save()
    else:
        comment_form=CommentForm()

    post_tags_ids=post_object.tags.values_list('id',flat=True)
    similar_posts = Post.objects.filter(
        tags__in=post_tags_ids).exclude(
        id=post_object.id)
    similar_posts = similar_posts.annotate(
        same_tags=Count('tags')).order_by(
        '-same_tags', '-publish')[:4]
    return render(request, 'blog/post/detail.html',
                  {'post': post_object,
                   'post_points': post_points,
                   'comments':comments,
                   'new_comment':new_comment,
                   'comment_form':comment_form,
                   'similar_posts':similar_posts})


def post_share(request,post_id):
    post=get_object_or_404(Post,id=post_id,
                       status='published')
    sent=False
    if request.method=='POST':
        form=EmailPostForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            post_url=request.build_absolute_uri(
                post.get_absolute_url())
            subject='{} ({}) рекомендует вам прочитать {}'.format(
                cd['name'],cd['email'],post.title)
            message='''Прочитай  "{}" по {}  
Коментарий: {} '''.format(post.title,post_url,cd['comments'])
            send_mail(subject,message,'admin@myblog.com',
                      [cd['to']])
            sent=True
    else:
        form=EmailPostForm()
    return render(request,
                  'blog/post/share.html',
                  {'post':post,
                   'form':form,
                   'sent':sent})
#TODO: pip install django-taggit
# python manage.py shell
# >>> from blog.models import Post
# >>> post=Post.objects.get(id=9)
# >>> post.tags.add('супы','вкусняхи')
# >>> post.tags.all()
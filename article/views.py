from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q


from .forms import CommentForm
from .models import (
                    Article,
                    Category,
                    Tag,
                    Comment,
                            )


def article_list(request):
    articles = Article.objects.order_by('-id')
    category = request.GET.get('cat')
    tag = request.GET.get('tag')
    q = request.GET.get('q')
    if q:
        q = Q(title__icontains=q)
        articles = articles.filter(q).order_by('-id')
    if category:
        articles = articles.filter(category__title__exact=category)
    if tag:
        articles = articles.filter(tags__title__exact=tag)
    paginator = Paginator(articles, 6)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    context = {
        'articles': articles,
    }
    return render(request, 'article/blog.html', context)


def article_detail(request, slug):
    form = CommentForm()
    articles = Article.objects.order_by('-id')[:3]
    article = get_object_or_404(Article, slug=slug)
    tags = Tag.objects.all()
    categories = Category.objects.all()
    comments = Comment.objects.filter(article_id=article.id, top_level_comment_id__isnull=True)
    cid = request.GET.get('cid')
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.article = article
            form.parent_id = cid
            form.save()
            messages.success(request, 'Comment submitted')
            return redirect('.#comment-form-replay')

    context = {
        'article': article,
        'categories': categories,
        'tags': tags,
        'comments': comments,
        'articles': articles,
        'form': form,

    }
    return render(request, 'article/single.html', context)
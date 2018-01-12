from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.


# 响应  localhost:8000/blog/index
def index(request):
    # return HttpResponse("hello world")
    # all 返回的就是一个django封装的类似于list的结果集，直接可用于循环
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def show_article(request, article_id):
    article = models.Article.objects.get(id=article_id)
    return render(request, 'blog/articlePage.html', {'article': article})


def edit_article(request, article_id):
    if article_id == '0':
        return render(request, 'blog/editArticle.html')
    article = models.Article.objects.get(id=article_id)
    return render(request, 'blog/editArticle.html', {'article': article})


def edit_action(request):
    # 分情况，若是新建就是create，若是更改则是save对象
    title = request.POST['title']
    content = request.POST['content']
    article_id = request.POST['article_id']
    if article_id == '0':
        article = models.Article.objects.create(title=title, content=content)
        return render(request, 'blog/articlePage.html', {'article': article})
    else:
        article = models.Article.objects.get(id=article_id)
        article.title = title
        article.content = content
        article.save()
        return render(request, 'blog/articlePage.html', {'article': article})
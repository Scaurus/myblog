# coding: utf-8
from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template  # получение шаблона
from django.template import Context  # хранение переменных
from django.shortcuts import render_to_response
from blog.models import Article, Comments



# Create your views here.


def homepage(request):
    view = "homepage"
    html = "<html><body>this is %s view </body></html>" % view
    return HttpResponse(html)


def homepage2(request):
    view = "homepage2"
    t = get_template('homepage.html')
    html = t.render(Context({'name': view}))
    return HttpResponse(html)


def homepage3(request):
    view = "homepage3"
    return render_to_response('homepage.html', {'name': view})


def articles(request):
    return render_to_response('articles.html', {'articles': Article.objects.all()})


def this_article(request,  article_id=1):
    return render_to_response('this_article.html',
                              {'article': Article.objects.get(id=article_id),
                               'comments': Comments.objects.filter(comments_article_id=article_id),
                               'article_id': Article.objects.get(id=article_id).id
                               })


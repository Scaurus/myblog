# coding: utf-8
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template  # получение шаблона
from django.template import Context  # хранение переменных
from django.shortcuts import render_to_response
from blog.models import Article, Comments
from blog.forms import CommentForm
from django.core.context_processors import csrf
from django.contrib import auth
from django.core.paginator import Paginator
import datetime


# Create your views here.
today = datetime.datetime.today()


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


def articles(request, page_number=1):
    all_articles = Article.objects.all()
    current_page = Paginator(all_articles, 3)
    return render_to_response('articles.html',
                              {'articles': current_page.page(page_number), 'username': auth.get_user(request).username})


# def this_article(request, article_id=1):
#     return render_to_response('this_article.html',
#                               {'article': Article.objects.get(id=article_id),
#                                'comments': Comments.objects.filter(comments_article_id=article_id),
#                                'article_id': Article.objects.get(id=article_id).id
#                                })

def this_article(request, article_id=1, comments_page_number=2):
    all_comments = Comments.objects.filter(comments_article_id=article_id)
    paginator = Paginator(all_comments, 2)
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = paginator.page(comments_page_number)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('this_article.html', args)


def addlike(request, article_id):
    try:
        if article_id in request.COOKIES:
            redirect('/')
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes += 1
            article.save()
            response = redirect('/')
            response.set_cookie(article_id, today)
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')


def addcomment(request, article_id):
    if request.POST and ('pause') not in request.session:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True

    return redirect('/articles/get/%s/' % article_id)

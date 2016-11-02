# -*- coding: UTF-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from article.models import Article


# Create your views here.
def home(request):
    post_list = Article.objects.all()  # 获取全部文章
    return render(request, 'article/base.html', {"post_list": post_list})


def detail(request, id):
    post = get_object_or_404(Article, pk=id)
    return render(request, 'article/base.html', {"post": post})
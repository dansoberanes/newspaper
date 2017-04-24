from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Article

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'content/article_list.html', {'articles': articles})

def home(request):
    articles = Article.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request, 'content/home.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'content/article_detail.html', {'article': article})

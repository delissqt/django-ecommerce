from django.shortcuts import render, get_object_or_404

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

# Create your views here.

from .models import Article


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all() # <blog>/<model_name>_list.html


class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    queryset = Article.objects.all()

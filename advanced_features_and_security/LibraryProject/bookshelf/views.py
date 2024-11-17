from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article

@permission_required('app_name.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

@permission_required('app_name.can_create', raise_exception=True)
def article_create(request):
    if request.method == "POST":
        # Logic to create article
        pass
    return render(request, 'article_form.html')

@permission_required('app_name.can_edit', raise_exception=True)
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        # Logic to edit article
        pass
    return render(request, 'article_form.html', {'article': article})

@permission_required('app_name.can_delete', raise_exception=True)
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('article_list')
"book_list", "books"
from .forms import ExampleForm

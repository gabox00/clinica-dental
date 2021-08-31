from django.shortcuts import render, get_object_or_404
from blog.models import Category, Article
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def getArticles(request):

    #Sacar articulos
    articles = Article.objects.all()

    #Paginar articulos
    paginator = Paginator(articles, 2)

    #recoger numero pagina
    page = request.GET.get('page')
    pageArticles = paginator.get_page(page)

    return render(request, "articles/list_articles.html", {
        "articles": pageArticles
    })

@login_required(login_url="login")
def getCategory(request, categoryID):

    category = get_object_or_404(Category, id=categoryID)
    articles =  Article.objects.filter(categories=categoryID)
    
    return render(request, "categories/category.html",{
        "category": category,
        "articles": articles
    })
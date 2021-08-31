from blog.models import Category, Article

def getCategories(request):
    
    ids = Article.objects.filter(public=True).values_list('categories',flat=True)
    categories = Category.objects.all()

    return({
        'categories': categories,
        'ids': ids
    })
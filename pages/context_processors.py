from pages.models import Page

def getPages(request):

    pages = Page.objects.filter(visible=True).order_by('order').all()

    return {
        'pages': pages
    }
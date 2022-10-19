from django.shortcuts import render
from shop.models import Item, ProductCategory
from blog.models import Blog
from cart.models import Cart
from django.views.generic import DetailView

def index(request):
    posts = Blog.objects.all().order_by('date_posted')
    recent_posts = posts[0:2]
    categories = ProductCategory.objects.all()
    items = Item.objects.all()


    return render(request, 'index.html', {'recent_posts' : recent_posts, 'categories':categories, 'items':items })


class QuickView(DetailView):
    model = Item
    template_name = 'quickview.html'
    context_object_name = 'item'


    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data

def test(request):
    items = Item.objects.all()

    return render(request, 'cllect.html', { 'items':items })


def description(request):

    return render(request, 'short-description.html')

def compare(request):

    return render(request, 'compare.html')


def page_not_found_view(request, exception):
    return render(request, "errors/404.html")

def error_view(request, exception):
    return render(request, "errors/403.html")

def permission_denied_view(request, exception):
    return render(request, "errors/400.html")

def bad_request_view(request, exception=None):
    return render(request, "errors/500.html")

from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog.urls')),
    path('pages/', include('pages.urls')),
    path('product/', include('product.urls')),
    path('shop/', include('shop.urls')),
    path('cart/', include('cart.urls')),
    path('', views.index ,name='index'),
    path("wishlist", views.wishlist, name="wishlist")
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

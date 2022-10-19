from django.contrib import admin
from django.urls import path, include
from . import views
from .views import QuickView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
# from django.conf.urls import handler400, handler403, handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog.urls')),
    path('pages/', include('pages.urls')),
    path('shop/', include('shop.urls')),
    path('cart/', include('cart.urls')),
    path('', views.index ,name='index'),
    path("short-description", views.description, name="short-description"),
    path("compare", views.compare, name="compare"),
    path('quickview/<int:pk>/', QuickView.as_view(), name='quickview'),
    path("test", views.test, name="test"),
]

handler404 = "belle.views.page_not_found_view" 
handler403 = 'belle.views.error_view'
handler400 = 'belle.views.permission_denied_view'
handler500 = 'belle.views.bad_request_view'

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

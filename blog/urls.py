from django.urls import path
from .views import (
    BlogView,
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    postpreference,
    # post_list
    )
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


app_name = 'blog'

urlpatterns = [
    path('', views.BlogView, name='home'),
    path('category/<str:name>', BlogListView.as_view(), name='blog-category'),
    path('blog/new/', BlogCreateView.as_view(), name='post-create'),
    # path('detail/<int:pk>/', views.BlogDetailView, name='post-detail'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='post-detail'),
    path('blog/<int:pk>/update/', BlogUpdateView.as_view(), name='post-update'),
    path('blog/<int:pk>/del/', BlogDeleteView.as_view(), name='post-delete'),
    path('blog/<int:postid>/preference/<int:userpreference>', postpreference, name='postpreference'),
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
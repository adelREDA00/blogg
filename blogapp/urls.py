from django.urls import path
from .views import HomeView,ArticleDetailView,AddpostView,UpdatePostViwe,DeletePost,AddcategoryView,CategoryView,LikeView
from . import views

urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(),name='article-detail'),
    path('add_post', AddpostView.as_view(),name='add_post'),
    path('article/edit/<int:pk>', UpdatePostViwe.as_view(),name='update_post'),
    path('article/<int:pk>/delete',DeletePost.as_view(),name='delete_post'),
    path('add_category',AddcategoryView.as_view(),name='add_category'),
    path('category/<str:cats>', CategoryView,name='category'),
    path('like/<int:pk>',LikeView,name='like_post'),
]
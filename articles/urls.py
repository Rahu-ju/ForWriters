from django.urls import path
from . import views

urlpatterns = [
    #Article urls
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('create/', views.ArticleCreateView.as_view(), name ='article_create'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name ='article_detail'),
    path('edit/<int:pk>/', views.ArticleUpdateView.as_view(), name='article_edit'),
    path('delete/<int:pk>/', views.ArticleDeleteView.as_view(), name='article_delete'),
    #comment urls
    path('comment/<int:pk>/', views.CommentCreateView.as_view(), name='comment'),
    path('comment/reply/<int:pk>/', views.ReplyCreateView.as_view(), name='reply'),
]

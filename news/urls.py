from django.urls import path
from .views import NewsList, NewsDetail, Search, NewsCreateView, NewsUpdateView, NewsDeleteView

urlpatterns = [
    path('', NewsList.as_view(), name='post_list'),
    path('<int:pk>', NewsDetail.as_view(), name='post'),
    path('search/', Search.as_view(), name='news_search'),
    path('add/', NewsCreateView.as_view(), name='news_create'),
    path('<int:pk>/edit/', NewsUpdateView.as_view(), name='news_edit'),
    path('<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    
]
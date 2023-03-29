from django.urls import path
from .views import ArticleList, ArticleItem

urlpatterns = [
    path('articles/', ArticleList.as_view()),
    path('articles/<int:pk>/', ArticleItem.as_view())
]
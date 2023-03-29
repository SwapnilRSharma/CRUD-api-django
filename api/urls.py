from django.urls import path
from .views import Articles, ArticleDetails

urlpatterns = [
    path('articles/', Articles.as_view()),
    path('articles/<int:pk>/', ArticleDetails.as_view())
]
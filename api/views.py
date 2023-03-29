from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer

class ArticleList(generics.ListCreateAPIView):
    serializer_class=ArticleSerializer

    def get_queryset(self):
        return Article.objects.all()
    
class ArticleItem(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=ArticleSerializer
    queryset = Article.objects.all()
from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework import status, generics
import math
from datetime import datetime

class Articles(generics.GenericAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        articles = Article.objects.all()
        total_articles = articles.count()
        if search_param:
            articles = articles.filter(name__icontains=search_param)
        serializer = self.serializer_class(articles[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_articles,
            "page": page_num,
            "last_page": math.ceil(total_articles / limit_num),
            "articles": serializer.data
        })
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "article": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        

class ArticleDetails(generics.GenericAPIView):
    serializer_class=ArticleSerializer
    queryset=Article.objects.all()

    def get_article(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        article = self.get_article(pk=pk)
        if article == None:
            return Response({"status": "fail", "message": f"Article with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(article)
        return Response({"status": "success", "article": serializer.data})

    def patch(self, request, pk):
        article = self.get_article(pk)
        if article == None:
            return Response({"status": "fail", "message": f"Article with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "article": serializer.data})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_article(pk)
        if article == None:
            return Response({"status": "fail", "message": f"Article with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        


    
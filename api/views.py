from main import models
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import serializers

# ----- INDEX -----
@api_view(['GET'])
def index(request):
    try:
        categories_serializer = serializers.ListCategorySerializer(models.Category.objects.all(), many=True)
        regions_serializer = serializers.ListRegionSerializer(models.Region.objects.all(), many=True)
        news_serializer = serializers.ListNewSerializer(models.New.objects.all(), many=True)
        return Response(
            {
                'categories_serializer':categories_serializer.data,
                'regions_serializer':regions_serializer.data,
                'news_serializer':news_serializer.data,
            }
        )
    except:
        return Response({'status':False})

# ----- CATEGORY -----
@api_view(['GET'])
def list_category(request):
    try:
        context = serializers.ListCategorySerializer(models.Category.objects.all(), many=True)
        return Response(context.data)
    except:
        return Response({'status':False})

@api_view(['GET'])
def detail_category(request, id):
    try:
        context = serializers.DetailCategorySerializer(models.Category.objects.get(id=id))
        return Response(context.data)
    except:
        return Response({'status':False})

# ----- REGION -----
@api_view(['GET'])
def list_region(request):
    try:
        context = serializers.ListRegionSerializer(models.Region.objects.all(), many=True)
        return Response(context.data)
    except:
        return Response({'status':False})

@api_view(['GET'])
def detail_region(request, id):
    try:
        context = serializers.DetailRegionSerializer(models.Region.objects.get(id=id))
        return Response(context.data)
    except:
        return Response({'status':False})

# ----- NEW -----
@api_view(['GET'])
def list_new(request):
    try:
        news = serializers.ListNewSerializer(models.New.objects.all(), many=True)
        return Response(news.data)
    except:
        return Response({'status':False})

@api_view(['GET'])
def detail_new(request, id):
    try:
        new = serializers.DetailNewSerializer(models.New.objects.get(id=id))
        return Response(new.data)
    except:
        return Response({'status':False})

@api_view(['GET'])
def list_new_category(request, id):
    try:
        categories_serializer = serializers.ListCategorySerializer(models.Category.objects.all(), many=True)
        regions_serializer = serializers.ListRegionSerializer(models.Region.objects.all(), many=True)
        news_serializer = serializers.ListNewSerializer(models.New.objects.filter(category=models.Category.objects.get(id=id)), many=True)
        return Response(
            {
                'categories_serializer':categories_serializer.data,
                'regions_serializer':regions_serializer.data,
                'news_serializer':news_serializer.data,
            }
        )
    except:
        return Response({'status':False})

@api_view(['GET'])
def list_new_region(request, id):
    try:
        categories_serializer = serializers.ListCategorySerializer(models.Category.objects.all(), many=True)
        regions_serializer = serializers.ListRegionSerializer(models.Region.objects.all(), many=True)
        news_serializer = serializers.ListNewSerializer(models.New.objects.filter(region=models.Region.objects.get(id=id)), many=True)
        return Response(
            {
                'categories_serializer':categories_serializer.data,
                'regions_serializer':regions_serializer.data,
                'news_serializer':news_serializer.data,
            }
        )
    except:
        return Response({'status':False})

# ----- COMMENT -----
@api_view(['POST'])
def create_comment(request, id):
    try:
        if request.method == 'POST':
            models.Comment.objects.create(
                new = models.New.objects.get(id=id),
                text = request.data.get('text'),
            )
            return Response({'status':True})
    except:
        return Response({'status':False})
    
@api_view(['GET'])
def list_comment_new(request, id):
    try:
        comments_serializer = serializers.ListCommentSerializer(models.Comment.objects.filter(new=models.New.objects.get(id=id)), many=True)
        return Response({'comments_serializer':comments_serializer.data})
    except:
        return Response({'status':False})
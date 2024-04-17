from main import models
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import serializers

# ----- CATEGORY -----
@api_view(['GET'])
def list_category(request):
    context = serializers.ListCategorySerializer(models.Category.objects.all(), many=True)
    return Response(context.data)

@api_view(['GET'])
def detail_category(request, id):
    context = serializers.DetailCategorySerializer(models.Category.objects.get(id=id))
    return Response(context.data)

# ----- REGION -----
@api_view(['GET'])
def list_region(request):
    context = serializers.ListRegionSerializer(models.Region.objects.all(), many=True)
    return Response(context.data)

@api_view(['GET'])
def detail_region(request, id):
    context = serializers.DetailRegionSerializer(models.Region.objects.get(id=id))
    return Response(context.data)

# ----- NEW -----
@api_view(['GET'])
def list_new(request):
    context = serializers.ListNewSerializer(models.New.objects.all(), many=True)
    return Response(context.data)

@api_view(['GET'])
def detail_new(request, id):
    context = serializers.DetailNewSerializer(models.New.objects.get(id=id))
    return Response(context.data)
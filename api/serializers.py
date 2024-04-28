from rest_framework.serializers import ModelSerializer
from main import models


# ----- CATEGORY -----
class ListCategorySerializer(ModelSerializer):
    class Meta:
        model = models.Category
        exclude = ['id']


class DetailCategorySerializer(ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


# ----- REGION -----
class ListRegionSerializer(ModelSerializer):
    class Meta:
        model = models.Region
        exclude = ['id']


class DetailRegionSerializer(ModelSerializer):
    class Meta:
        model = models.Region
        fields = '__all__'


# ----- NEW -----
class ListNewSerializer(ModelSerializer):
    class Meta:
        model = models.New
        fields = '__all__'
        # exclude = ['id']
        depth = 1


class DetailNewSerializer(ModelSerializer):
    class Meta:
        model = models.New
        fields = ['id', 'title', 'body', 'banner_image', 'author', 'category', 'region', 'date', 'images', 'videos']
        depth = 1


# ----- COMMENT -----
class ListCommentSerializer(ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ['new', 'text', 'date']
        depth = 2






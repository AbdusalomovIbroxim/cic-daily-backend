from rest_framework import serializers
from .models import (TeamMembersModel, AuthorArticlesModel, 
                     ArticlesModel, CategoryArticlesModel)
from django.shortcuts import get_object_or_404

class TeamMembersSerializer(serializers.Serializer):
    class Meta:
        model = TeamMembersModel
        fields = ('full_name', 'age', 'position', 'description')

class AuthorArticlesSerializer(serializers.Serializer):
    class Meta:
        model = AuthorArticlesModel
        fields = ('full_name',)

class CategoryArticlesSerialzier(serializers.Serializer):
    class Meta:
        model = CategoryArticlesModel
        fields = ('name',)

class ArticlesSerializer(serializers.Serializer):
    class Meta:
        model = ArticlesModel 
        fields = ('category', 'title','content','author')


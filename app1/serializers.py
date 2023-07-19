from rest_framework import serializers
from .models import (TeamMembersModel, AuthorArticlesModel, 
                     ArticlesModel, CategoryArticlesModel)
from django.shortcuts import get_object_or_404

class TeamMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMembersModel
        fields = ('full_name', 'age', 'position', 'description')

class AuthorArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorArticlesModel
        fields = ('full_name',)

class CategoryArticlesSerialzier(serializers.ModelSerializer):
    class Meta:
        model = CategoryArticlesModel
        fields = ('name',)

class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticlesModel 
        fields = ('category', 'title','content','author')


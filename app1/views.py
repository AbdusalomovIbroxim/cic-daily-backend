from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ArticlesModel, TeamMembersModel, AuthorArticlesModel, CategoryArticlesModel
from rest_framework import status
from .serializers import (TeamMembersSerializer, AuthorArticlesSerializer,
                          CategoryArticlesSerialzier, ArticlesSerializer)
from rest_framework import generics

#-------TEAM MEMBER VIEWS STARTED--------

class LCTeamMemberView(generics.ListCreateAPIView):
    queryset = TeamMembersModel.objects.all()
    serializer_class = TeamMembersSerializer

class RUDTeamMemberView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeamMembersModel.objects.all()
    serializer_class = TeamMembersSerializer

#-------TEAM MEMBER VIEWS FINISHED--------   


#------ARTICLE VIEWS STARTED------

#Author articles CRUD
class LCAuthorArticlesView(generics.ListCreateAPIView):
    queryset = AuthorArticlesModel.objects.all()
    serializer_class = AuthorArticlesSerializer
    
class RUDAuthorArticlesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuthorArticlesModel.objects.all()
    serializer_class = AuthorArticlesSerializer
    

#Category articles CRUD
class LCCategoryArticlesView(generics.ListCreateAPIView):
    queryset = CategoryArticlesModel.objects.all()
    serializer_class = CategoryArticlesSerialzier
    
class RUDCategoryArticlesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryArticlesModel.objects.all()
    serializer_class = CategoryArticlesModel

#Articles CRUD
class LCArticlesView(generics.ListCreateAPIView):
    queryset = ArticlesModel.objects.all()
    serializer_class = ArticlesSerializer

class RUDArticlesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArticlesModel.objects.all()
    serializer_class = ArticlesSerializer



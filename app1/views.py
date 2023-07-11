from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ArticlesModel, TeamMembersModel, AuthorArticlesModel, CategoryArticlesModel
from rest_framework import status
from .serializers import (TeamMembersSerializer, AuthorArticlesSerializer,
                          CategoryArticlesSerialzier, ArticlesSerializer)
from rest_framework import generics

#-------TEAM MEMBER VIEWS STARTED--------

# Team Member CRUD
# class AllTeamMemberView(APIView):
#     def get(self,request,*args,**kwargs):
#         all_member = TeamMembersModel.objects.all()
#         serializer = TeamMembersSerializer(all_member)
#         return Response(serializer.data)

# class CreateTeamMemberView(APIView):
#     def post(self,request,*args,**kwargs):
#         serializer = TeamMembersSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LCTeamMemberView(generics.ListCreateAPIView):
    queryset = TeamMembersModel.objects.all()
    serializer_class = TeamMembersSerializer
    # permission_classes = (permissions.IsAuthenticated,)

class RUDTeamMemberView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeamMembersModel.objects.all()
    serializer_class = TeamMembersSerializer
    # permission_classes = (permissions.IsAuthenticated,)

# class ReadTeamMemberView(APIView):
#     def get(self,request,*args,**kwargs):
#         data = get_object_or_404(TeamMembersModel, pk=kwargs['team_member_id'])
#         serializer = TeamMembersSerializer(data)
#         return Response(serializer.data)

# class UpdateTeamMemberView(APIView):
#     def patch(self,request,*args,**kwargs):
#         instance = get_object_or_404(TeamMembersModel, pk=kwargs['team_member_id'])
#         serializer = TeamMembersSerializer(instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#  

 
# class DeleteTeamMemberView(APIView):
#     def delete(self,request,*args,**kwargs):
#         instance = get_object_or_404(TeamMembersModel, pk=kwargs['team_member_id'])
#         instance.delete()
#         return Response({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

#-------TEAM MEMBER VIEWS FINISHED--------   


#-------------------------------------------------------------------


#------ARTICLE VIEWS STARTED------

#Author articles CRUD
class LCAuthorArticlesView(generics.ListCreateAPIView):
    queryset = AuthorArticlesModel.objects.all()
    serializer_class = AuthorArticlesSerializer
    # permission_classes = (permissions.IsAuthenticated,)

class RUDAuthorArticlesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuthorArticlesModel.objects.all()
    serializer_class = AuthorArticlesSerializer
    # permission_classes = (permissions.IsAuthenticated,)


# class AllAuthorArticlesView(APIView):
#     def get(self,request,*args,**kwargs):
#         all_data = AuthorArticlesModel.objects.all()
#         serialier = AuthorArticlesSerializer(all_data, many=False)
#         return Response(serialier.data)
    
# class CreateAuthorArticlesView(APIView):
#     def post(self,request,*args,**kwargs):
#         serializer = AuthorArticlesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class ReadAuthorArticlesView(APIView):
#     def get(self,request,*args,**kwargs):
#         data = get_object_or_404(AuthorArticlesModel, pk=kwargs['author_id'])
#         serializer = AuthorArticlesSerializer(data)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
# class UpdateAuthorArticlesView(APIView):
#     def patch(self,request,*args,**kwargs):
#         instance = get_object_or_404(AuthorArticlesModel, pk=kwargs['author_id'])
#         serializer = AuthorArticlesSerializer(instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class DeleteAuthorArticlesView(APIView):
    def delete(self,request,*args,**kwargs):
        instance = get_object_or_404(AuthorArticlesModel, pk=kwargs['author_id'])
        instance.delete()
        return Response({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)



#Category articles CRUD
class LCCategoryArticlesView(generics.ListCreateAPIView):
    queryset = CategoryArticlesModel.objects.all()
    serializer_class = CategoryArticlesSerialzier
    # permission_classes = (permissions.IsAuthenticated,)

class RUDCategoryArticlesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryArticlesModel.objects.all()
    serializer_class = CategoryArticlesModel
    # permission_classes = (permissions.IsAuthenticated,)

# class AllCategoryArticlesView(APIView):
#     def get(self,request,*args,**kwargs):
#         all_categ = CategoryArticlesModel.objects.all()
#         serializer = CategoryArticlesSerialzier(all_categ, many=False)
#         return Response(serializer.data)
    
# class CreateCategoryArticlesView(APIView):
#     def post(self,request,*args,**kwargs):
#         serializer = CategoryArticlesSerialzier(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ReadCategoryArticlesView(APIView):
#     def get(self,request,*args,**kwargs):
#         data = get_object_or_404(CategoryArticlesModel, pk=kwargs['category_id'])
#         serializer = CategoryArticlesSerialzier(data)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
# class UpdateCategoryArticlesView(APIView):
#     def patch(self,request,*args,**kwargs):
#         instance = get_object_or_404(CategoryArticlesModel, pk=kwargs['category_id'])
#         serializer = CategoryArticlesSerialzier(instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class DeleteCategoryArticlesView(APIView):
#     def delete(self,request,*args,**kwargs):
#         instance = get_object_or_404(CategoryArticlesModel, pk=kwargs['category_id'])
#         instance.delete()
#         return Response({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)



#Articles CRUD
class LCArticlesView(generics.ListCreateAPIView):
    queryset = ArticlesModel.objects.all()
    serializer_class = ArticlesSerializer
    # permission_classes = (permissions.IsAuthenticated,)

class RUDArticlesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArticlesModel.objects.all()
    serializer_class = ArticlesSerializer
    # permission_classes = (permissions.IsAuthenticated,)

# class AllArticlesView(APIView):
#     def get(self,request,*args, **kwargs):
#         all_data = ArticlesModel.objects.all()
#         serializer = ArticlesSerializer(all_data, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
# class CreateArticlesView(APIView):
#     def post(self,request,*args,**kwargs):
#         serializer = ArticlesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ReadArticlesView(APIView):
#     def get(self,request,*args,**kwargs):
#         data = get_object_or_404(ArticlesModel, pk=kwargs['article_id'])
#         serializer = ArticlesSerializer(data)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
# class UpdateArticlesView(APIView):
#     def patch(self,request,*args,**kwargs):
#         instance = get_object_or_404(ArticlesModel, pk=kwargs['article_id'])
#         serializer = ArticlesSerializer(instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class DeleteArticlesView(APIView):
#     def delete(self,request,*args,**kwargs):
#         instance = get_object_or_404(ArticlesModel, pk=kwargs['article_id'])
#         instance.delete
#         return Response({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    

#-----ARTICLE VIEWS FINISHED--------




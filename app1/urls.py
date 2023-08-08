from django.urls import path
from .views import (LCTeamMemberView,RUDTeamMemberView,
                    LCAuthorArticlesView, RUDAuthorArticlesView,
                    LCCategoryArticlesView, RUDCategoryArticlesView,
                    LCArticlesView, RUDArticlesView)
#               
#                     
urlpatterns = [
    #Team Member urls
    path('member/', LCTeamMemberView.as_view()),
    path('member/<pk>', RUDTeamMemberView.as_view()),
   
    #Author Articles urls
    path('author/', LCAuthorArticlesView.as_view()),
    path('author/<pk>', RUDAuthorArticlesView.as_view()),
  
    #Category Articles urls
    path('category/', LCCategoryArticlesView.as_view()),
    path('category/<pk>', RUDCategoryArticlesView.as_view()),
  
    #Articles urls
    path('article/', LCArticlesView.as_view()),
    path('article/<pk>', RUDArticlesView.as_view()),
    
]
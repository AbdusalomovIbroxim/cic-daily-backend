from django.urls import path
from .views import (LCTeamMemberView,RUDTeamMemberView,
                    LCAuthorArticlesView, RUDAuthorArticlesView,
                    LCCategoryArticlesView, RUDCategoryArticlesView,
                    LCArticlesView, RUDArticlesView)
#               
#                     ReadTeamMemberView,
#                     UpdateTeamMemberView, DeleteTeamMemberView, AllCategoryArticlesView,
#                     ReadCategoryArticlesView,UpdateCategoryArticlesView,DeleteCategoryArticlesView,
#                     CreateCategoryArticlesView, AllAuthorArticlesView,ReadAuthorArticlesView,
#                     CreateAuthorArticlesView, UpdateAuthorArticlesView, DeleteAuthorArticlesView,
#                     AllArticlesView, ReadArticlesView, CreateArticlesView, 
#                     UpdateArticlesView, DeleteArticlesView)
urlpatterns = [
    #Team Member urls
    path('member/', LCTeamMemberView.as_view()),
    path('member/<pk>', RUDTeamMemberView.as_view()),
    # path('member/create/', CreateTeamMemberView.as_view()),
    # path('member/<int:team_member_id>/', ReadTeamMemberView.as_view()),
    # path('member/update/<int:team_member_id>/', UpdateTeamMemberView.as_view()),
    # path('delete/<int:team_member_id>/', DeleteTeamMemberView.as_view()),

    #Author Articles urls
    path('author/', LCAuthorArticlesView.as_view()),
    path('author/<pk>', RUDAuthorArticlesView.as_view()),
    # path('author/create/', CreateAuthorArticlesView.as_view()),
    # path('author/<int:author_id>/', ReadAuthorArticlesView.as_view()),
    # path('author/update/<int:author_id>/', UpdateAuthorArticlesView.as_view()),
    # path('author/delete/<int:author_id>/', DeleteAuthorArticlesView.as_view()),

    #Category Articles urls
    path('category/', LCCategoryArticlesView.as_view()),
    path('category/<pk>', RUDCategoryArticlesView.as_view()),
    # path('category/<int:category_id>/', ReadCategoryArticlesView.as_view()),
    # path('category/update/<int:category_id>/', UpdateCategoryArticlesView.as_view()),
    # path('category/create/', CreateCategoryArticlesView.as_view()),
    # path('category/delete/<int:category_id>/', DeleteCategoryArticlesView.as_view()),

    #Articles urls
    path('article/', LCArticlesView.as_view()),
    path('article/<pk>', RUDArticlesView.as_view()),
    # path('article/<int:article_id>/', ReadArticlesView.as_view()),
    # path('article/create/', CreateArticlesView.as_view()),
    # path('article/update/<int:article_id>/', UpdateArticlesView.as_view()),
    # path('article/delete/<int:article_id>/', DeleteArticlesView.as_view()),

]
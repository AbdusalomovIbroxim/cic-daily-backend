from django.contrib import admin
from .models import ArticlesModel,CategoryArticlesModel,TeamMembersModel,AuthorArticlesModel

admin.site.register(ArticlesModel),
admin.site.register(CategoryArticlesModel),
admin.site.register(TeamMembersModel),
admin.site.register(AuthorArticlesModel),
# Register your models here.

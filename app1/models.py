from django.db import models
from datetime import datetime

#Team members model
class TeamMembersModel(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField(default=18)
    position = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self) -> str:
        return self.full_name
    
    class Meta:
        db_table = 'team_member'

#Articles model
class AuthorArticlesModel(models.Model):
    full_name = models.ForeignKey(TeamMembersModel, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'author'

class CategoryArticlesModel(models.Model):
    name = models.CharField(max_length=100, default='Not given')

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'category'

class ArticlesModel(models.Model):
    category = models.ForeignKey(CategoryArticlesModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField(default='None')
    content = models.TextField(default='None')
    author = models.ForeignKey(AuthorArticlesModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = 'article'

#Events model
class EventModel(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = 'event'

    
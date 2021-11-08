from django.db import models

class TodosSchema(models.Model) :
    todo_title = models.CharField(max_length=140,null=True,blank=True)
    todo_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
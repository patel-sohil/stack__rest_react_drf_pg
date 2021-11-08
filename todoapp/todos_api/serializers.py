from .models import TodosSchema
from rest_framework.serializers import ModelSerializer

class TodoSerializer(ModelSerializer) :
    class Meta :
        model = TodosSchema
        fields = "__all__"
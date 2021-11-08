from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from datetime import datetime

class TestSetUp(APITestCase) :
    
    def setUp(self) :
        self.todos_get_url = reverse('todosschema-list')
        self.todos_post_url = reverse('todosschema-list')        

        self.todo_sample_data = {
            'todo_title':'Install Django Rest Framework',
            'todo_description':'Check DRF documentation',
            'created_at':datetime.now(),
            'status':'In Progress'
        }

        return super().setUp()
    
    def tearDown(self) :
        return super().tearDown()
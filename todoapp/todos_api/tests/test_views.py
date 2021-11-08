from .test_setup import TestSetUp
from rest_framework import status

class TestViews(TestSetUp) :
    
    def test_todo_get(self) :
        resp = self.client.get(self.todos_get_url)
        self.assertEqual(resp.data, [])
        self.assertTrue(status.is_success(status.HTTP_200_OK))

    def test_todo_post(self) :
        resp = self.client.post(self.todos_post_url,self.todo_sample_data,format="json")

        for field, fieldvalue in self.todo_sample_data.items() :
            if field == "id" :
                self.assertIsInstance(fieldvalue,int)
            elif field != "created_at" :
                self.assertEqual(resp.data[field], str(fieldvalue))

        self.assertTrue(status.is_success(status.HTTP_201_CREATED))
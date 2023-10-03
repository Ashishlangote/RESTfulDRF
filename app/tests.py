from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class HomePageTestCase(APITestCase):
    def test_home_page(self):
        response = self.client.get(reverse('home_page'))
        print(response)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data["message"],"Welcome to home page")

class PostListTestCase(APITestCase):
    

    def authenticate(self):

        self.client.post(reverse("signup"),{
            "email": "test01@example.com",
            "username": "test01user",
            "password": "test1234",
        })

        response = self.client.post(reverse("login"),{
            "email": "test01@example.com",
            "password": "test1234",
        })
        print(response.data)

        token = response.data['token']['access']
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    def test_posts_list(self):

        self.authenticate()
        response = self.client.get(reverse("posts-list"))
        print(response)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
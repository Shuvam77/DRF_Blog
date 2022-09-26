from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Category
from django.contrib.auth.models import User
from rest_framework.test import APIClient

# Create your tests here.


class PostTest(APITestCase):
    
    def test_view_posts(self):
        url = reverse('api_blog:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def create_post(self):
        self.test_category = Category.objects.create(name='django')
        self.testuser1 = User.objects.create_superuser(username='test_user1', password='123456789')

    
        self.client.login(username=self.testuser1.username,
                          password='123456789')

        data = {'title':'new', 'author':1, 'excerpt':'new', 'content':'new'}
        url = reverse('api_blog:listcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_update(self):
        client = APIClient()
        self.test_category = Category.objects.create(name='django')
        self.testuser1 = User.objects.create_user(username='test_user1', password='123456789')
        self.testuser2 = User.objects.create_user(username='test_user2', password='123456789')
        test_post = Post.objects.create(category_id=1, title = 'title',content='something', excerpt='anything', slug='title', author_id=1, status='publish')

        client.login(username = 'test_user1', password = '123456789')
        url = reverse('api_blog:updatepost', kwargs={'pk':1})
        response = client.put(
            url, {
                "title":"new title",
                "author":1,
                "excerpt":"new thing",
                "content": "very very new thing",
                "status": "publish"
            }, format='json'
        )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


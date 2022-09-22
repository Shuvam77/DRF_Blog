from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category
# Create your tests here.


class Test_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        testuser1 = User.objects.create(username='testuser1', password='12345@team')
        test_post1 = Post.objects.create(category_id=1, title = 'title',content='something', excerpt='anything', slug='title', author_id=1, status='publish' )


    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        cat= Category.objects.get(id=1)

        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'

        self.assertEqual(author, 'testuser1')
        self.assertEqual(excerpt, 'anything')
        self.assertEqual(title, 'title')
        self.assertEqual(content, 'something')
        self.assertEqual(status, 'publish')
        self.assertEqual(str(post), 'title')
        self.assertEqual(str(cat), 'django')
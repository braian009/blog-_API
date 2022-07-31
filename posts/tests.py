from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post

# Create your tests here.

class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@email.com',
            password = 'secret',
        )
        self.post = Post.objects.create(
            title = 'A good title',
            author = self.user,
            body = 'Nice body content',
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertEqual(self.post.title, 'A good title')
        self.assertEqual(self.post.body, 'Nice body content')
        self.assertEqual(str(self.post), 'A good title')
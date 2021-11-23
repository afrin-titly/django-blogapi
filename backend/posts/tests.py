from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User

class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
      testuser1 = User.objects.create_user(username="user", password="secret123")
      testuser1.save()

      test_blog = Post.objects.create(author=testuser1, title="test title", body="test body..")
      test_blog.save()

    def test_blog_content(self):
      post = Post.objects.get(id=1)
      author = f'{post.author}'
      title = f'{post.title}'
      body = f'{post.body}'
      self.assertEqual(author, 'user')
      self.assertEqual(title, 'test title')
      self.assertEqual(body, 'test body..')



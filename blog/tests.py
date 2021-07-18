from django.test import TestCase
from .models import Post
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
class BlogTest(TestCase):

    def create_post(self, title="Test_Title", content="Test_Content"):
        user = User.objects.create(username='AnotherUser')
        return Post.objects.create(title=title, content=content, date_posted=timezone.now(), author=user)

    def test_Post_creation(self):
        P = self.create_post()
        self.assertTrue(isinstance(P, Post))
        self.assertEqual(P.__str__(), P.title)
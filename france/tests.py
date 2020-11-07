from django.test import TestCase
from django.urls import reverse


class TestFrance(TestCase):
    """Test all france app views"""

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_404_view(self):
        response = self.client.get('/test404')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '404.html')


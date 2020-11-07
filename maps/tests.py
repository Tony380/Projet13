from django.test import TestCase
from django.urls import reverse
from .models import Region, Department


class TestMaps(TestCase):
    """Test all maps app views"""

    def setUp(self):
        Region.objects.create()

    def test_france_view(self):
        response = self.client.get(reverse('maps:france'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'france.html')

    def test_region_view(self):
        region_id = Region.objects.first().id
        response = self.client.get(reverse('maps:region', args=[region_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'region.html')

    def test_department_view(self):
        region = Region.objects.first()
        department_id = Department.objects.create(region=region).id
        response = self.client.get(reverse('maps:department', args=[department_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'department.html')

    def test_department_paris_view(self):
        region = Region.objects.first()
        department_id = Department.objects.create(name='Ville de Paris', region=region).id
        response = self.client.get(reverse('maps:department', args=[department_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'department.html')

    def test_commune_view(self):
        response = self.client.get(reverse('maps:commune', args=['test']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'commune.html')

    def test_commune_paris_view(self):
        response = self.client.get(reverse('maps:commune', args=['Paris']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'commune.html')

    def test_region_string(self):
        region = Region.objects.create(name='test')
        self.assertEqual(str(region), 'test')

    def test_department_string(self):
        region = Region.objects.first()
        department = Department.objects.create(name='test_name', region=region)
        self.assertEqual(str(department), 'test_name')

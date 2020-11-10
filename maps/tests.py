from django.test import TestCase
from django.urls import reverse
from .models import Region, Department, User, Favorite


class TestMaps(TestCase):
    """Test all maps app views"""

    def setUp(self):
        Region.objects.create()

    def test_france_view(self):
        """Test france page"""
        response = self.client.get(reverse('maps:france'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'france.html')

    def test_region_view(self):
        """Test region page"""
        region_id = Region.objects.first().id
        response = self.client.get(reverse('maps:region',
                                           args=[region_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'region.html')

    def test_department_view(self):
        """Test department page"""
        region = Region.objects.first()
        department_id = Department.objects.create(
            region=region).id
        response = self.client.get(reverse('maps:department',
                                           args=[department_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'department.html')

    def test_department_paris_view(self):
        """Test Ville de Paris search"""
        region = Region.objects.first()
        department_id = Department.objects.create(
            name='Ville de Paris',
            region=region).id
        response = self.client.get(reverse('maps:department',
                                           args=[department_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'department.html')

    def test_commune_view(self):
        """Test commune page"""
        response = self.client.get(reverse('maps:commune',
                                           args=['test']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'commune.html')

    def test_commune_paris_view(self):
        """Test Paris search"""
        response = self.client.get(reverse('maps:commune',
                                           args=['Paris']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'commune.html')

    def test_save_view(self):
        """Test favorite not saved"""
        user = User.objects.create(username="name")
        self.client.force_login(user)
        response = self.client.post(reverse('maps:save',
                                            args=['title']),
                                    HTTP_REFERER='users:profile')
        self.assertEqual(response.status_code, 302)

    def test_save_fav_view(self):
        """Test favorite already saved"""
        user = User.objects.create(username="name")
        self.client.force_login(user)
        Favorite.objects.create(title='title', user_id=user.id)
        response = self.client.post(reverse('maps:save',
                                            args=['title']),
                                    HTTP_REFERER='users:profile')
        self.assertEqual(response.status_code, 302)

    def test_del_favorite_view(self):
        """Test delete favorite"""
        user = User.objects.create(username="name")
        self.client.force_login(user)
        Favorite.objects.create(title='title', user_id=user.id)
        response = self.client.post(reverse('maps:del_favorite',
                                            args=['title']),
                                    HTTP_REFERER='users:profile')
        self.assertEqual(response.status_code, 302)

    def test_region_string(self):
        """Test string method of region model"""
        region = Region.objects.create(name='test')
        self.assertEqual(str(region), 'test')

    def test_department_string(self):
        """Test string method of department model"""
        region = Region.objects.first()
        department = Department.objects.create(name='test_name',
                                               region=region)
        self.assertEqual(str(department), 'test_name')

    def test_favorite_string(self):
        """Test string method of favorite model"""
        user = User.objects.create_user('jack')
        favorite = Favorite.objects.create(title='test_name',
                                           user_id=user.id)
        self.assertEqual(str(favorite), 'test_name')

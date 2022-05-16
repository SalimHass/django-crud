from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Snack
from django.urls import reverse


class SnackPageViewTest(TestCase):
    def test_snack_list_status_check(self):
        url = reverse('snacks_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_list_template(self):
        url = reverse('snacks_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snacks_list.html')
        self.assertTemplateUsed(response, '_base.html')
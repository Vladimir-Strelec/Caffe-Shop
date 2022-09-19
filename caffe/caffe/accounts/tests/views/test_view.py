from django.test import TestCase
from django.urls import reverse

from caffe.accounts.models import Profile, ShopUser


class BaseViewTestCase(TestCase):
    VALID_PROFILE_DATA = {
        'first_name': 'Vova',
        'last_name': 'Strelec',
        'email': 'vovik050@mail.ru',
    }

    def test_expect_correct_template_UserRegisterView(self):
        response = self.client.get(reverse('register'))
        self.assertTemplateUsed(response, 'account/registration.html')

    def test_get_expect_correct_template_UserLoginView(self):
        response = self.client.get(reverse('login user'))
        self.assertTemplateUsed(response, 'account/login.html')


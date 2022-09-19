from django.test import TestCase

from caffe.accounts.forms import CreateProfileForm


class FormTestCase(TestCase):


    def test_create_profile_form(self):
        data = {
            'username': 'Test',
            'password1': 'v1',
            'password2': 'v1',
            'first_name': 'Test',
            'last_name': 'Testov',
        }

        form = CreateProfileForm(data)

        self.assertTrue(form.is_valid())
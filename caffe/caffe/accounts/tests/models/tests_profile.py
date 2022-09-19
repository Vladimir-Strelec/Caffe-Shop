from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from caffe.accounts.models import Profile, ShopUser

UserModel = get_user_model()


class ProfileTests(TestCase):


    VALID_PROFILE_DATA = {
        'first_name': 'Vova',
        'last_name': 'Strelec',
        'email': 'vovik050@mail.ru',
    }


    def test_profile_create__when_first_name_only_letters__expect_success(self):
        user = ShopUser.objects.create(username='Vovan', password='v1')
        profile = Profile.objects.create(user=user, **self.VALID_PROFILE_DATA)
        profile.full_clean()
        profile.save()
        self.assertIsNotNone(profile)

    def test_valid_character_with_name_profile(self):
        user = ShopUser.objects.create(username='Vovan', password='v1')
        profile = Profile.objects.create(user=user, **self.VALID_PROFILE_DATA)
        profile.first_name = '123'
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(context.exception)

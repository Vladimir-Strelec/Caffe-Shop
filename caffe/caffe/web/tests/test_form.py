from django.core.exceptions import ValidationError
from django.test import TestCase

from caffe.web.forms import CreateProductForm
from caffe.web.models import AbstractProduct


class FormTestCase(TestCase):
    VALID_DATE_PRODUCT = {'name': 'Test', 'price': 12, 'product_info': 'test info', 'remains': 5, 'image': 'mediafiles/bodi-raw-rxzqqwJhUr4-unsplash.jpg'}

    def test_create_product(self):
        product = AbstractProduct.objects.create(**self.VALID_DATE_PRODUCT)
        product.save()
        self.assertIsNotNone(product.pk)
        # self.assertEqual(f'{self.VALID_DATE_PRODUCT["name"]}', product.name)
        # self.assertEqual(self.VALID_DATE_PRODUCT["price"], product.price)
        # self.assertEqual(f'{self.VALID_DATE_PRODUCT["product_info"]}', product.product_info)
        # self.assertEqual(self.VALID_DATE_PRODUCT['remains'], product.remains)
        # self.assertEqual(f'{self.VALID_DATE_PRODUCT["image"]}', product.image)

    def test_valid_character(self):
        product = AbstractProduct.objects.create(**self.VALID_DATE_PRODUCT)
        product.name = 'Test1'
        with self.assertRaises(ValidationError) as context:
            product.full_clean()
            product.save()

        self.assertIsNotNone(context.exception)

from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from caffe.accounts.models import Profile
from common.validators import validate_only_letters


UserModel = get_user_model()


class AbstractProduct(models.Model):
    MAX_LEN_NAME = 30
    MIN_LEN_NAME = 2
    #

    name = models.CharField(
        max_length=MAX_LEN_NAME,
        validators=(MinLengthValidator(MIN_LEN_NAME),
                    validate_only_letters)
    )

    price = models.FloatField()

    product_info = models.TextField()

    # count = models.CharField(
    #     max_length=max(len(x) for (x, _) in TYPE_CHOICES),
    #     choices=TYPE_CHOICES,)

    remains = models.FloatField()

    image = models.ImageField(
        validators=(
            # validate_file_max_size_in_mb(5),
            # validate_file_max_size_in_mb(7),
            # validate_file_max_size_in_mb(8),
        )
    )


class CommentsProducts(models.Model):
    MAX_LEN_TEXT = 200
    MIN_LEN_TEXT = 2

    text = models.TextField()

    product = models.ForeignKey(AbstractProduct, on_delete=models.CASCADE)

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)


class Cart(models.Model):
    product = models.ForeignKey(AbstractProduct, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

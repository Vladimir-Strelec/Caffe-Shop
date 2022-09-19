from django.contrib import admin

from caffe.web.models import AbstractProduct, CommentsProducts


@admin.register(AbstractProduct)
class AbstractProductAdmin(admin.ModelAdmin):
    pass


@admin.register(CommentsProducts)
class AbstractProductAdmin(admin.ModelAdmin):
    pass

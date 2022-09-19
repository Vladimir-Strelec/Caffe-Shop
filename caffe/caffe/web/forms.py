from django import forms

from caffe.web.models import AbstractProduct, CommentsProducts, Cart
from common.helpers import BootstrapFormMixin


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = AbstractProduct
        fields = '__all__'


class EditProductForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = AbstractProduct
        fields = '__all__'


class DeleteProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, fild in self.fields.items():
            fild.widget.attrs['disabled'] = 'disabled'
            fild.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = AbstractProduct
        fields = '__all__'


class CreateReviewProductForm(forms.ModelForm):
    class Meta:
        model = CommentsProducts
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CreateCart(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ()


class ClearProductsUser(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Cart
        fields = ()
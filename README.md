![Header](https://thumbs.gfycat.com/AdmirableEvergreenDoe-size_restricted.gif)
___
# Django_Flashcards:nerd_face:
[![Flutter](https://img.shields.io/badge/-Link_to_this_app_on_heroku-000000?style=for-the-badge&)](https://webgame198890201.herokuapp.com/)
___
## *Languages and tools*

![](https://img.shields.io/static/v1?label=&message=PYTHON&color=black&style=for-the-badge&logo=python&logoColor=yellow)
![](https://img.shields.io/static/v1?label=&message=DJANGO&color=black&style=for-the-badge&logo=Django&logoColor=green)
![](https://img.shields.io/static/v1?label=&message=PosgreSQL&color=black&style=for-the-badge&logo=Postgresql&logoColor=3399ff)
![](https://img.shields.io/static/v1?label=&message=SQLITE&color=black&style=for-the-badge&logo=SQLITE&logoColor=red)
![](https://img.shields.io/static/v1?label=&message=Docker&color=black&style=for-the-badge&logo=Docker)
___
>APP INFO
>>This project was created by me from scratch to defend the Django exam. This is an imitation of a store with a customized user and all sorts of relationships for honing knowledge. In this project, the emphasis was not placed on the front-end, but I designed it using flexbox technology
___
## Technical points
>Creating a manger to create Custom User
>>*This code performs the function of redefining fields for User, for Name email and password, in my case. In this project, the emphasis was not placed on the front-end, but I designed it using flexbox technology*
```python
from django.contrib.auth.base_user import BaseUserManager 
from django.contrib.auth.hashers import make_password

class ShopUserManager(auth_base.BaseUserManager):
    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        user = self.model(username=username, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)
```
___
>Logic
* With the help of this code, I have achieved the ability to leave comments under each product.
```python
class AddComments(LoginRequiredMixin, views.CreateView):
    form_class = CreateReviewProductForm
    template_name = 'comments/add-comments.html'
    context_object_name = 'object'
    success_url = reverse_lazy('catalog')

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['id_product'] = self.kwargs['pk']
        return result

    def form_valid(self, form, **kwargs):
        form.instance.product = AbstractProduct.objects.get(pk=self.kwargs['pk'])
        form.instance.user = self.request.user
        result = super().form_valid(form)
        return result


class AllCommentsView(LoginRequiredMixin, auth_views.TemplateView):
    model = CommentsProducts
    template_name = 'comments/all-comments-product.html'

    def get_context_data(self, **kwargs):
        all_comments_in_product = sorted(set(CommentsProducts.objects.filter(product_id=kwargs['pk'])), key=lambda kvp: [-kvp.id])

        context = super().get_context_data(**kwargs)
        context['all_comments_in_product'] = all_comments_in_product
        return context
```
___
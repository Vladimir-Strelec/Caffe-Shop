from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as auth_views
from django.views import generic as views
from django.views.generic import DeleteView


from caffe.web.forms import CreateProductForm, EditProductForm, DeleteProductForm, CreateReviewProductForm, CreateCart, \
    ClearProductsUser
from caffe.web.models import AbstractProduct, CommentsProducts, Cart
from common.view_mixin import RedirectToCatalog


class HomeTemplateView(RedirectToCatalog, views.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['valid_register'] = False
        return context


class CreateProductView(auth_views.CreateView, PermissionRequiredMixin):
    permission_required = 'web.add_abstractproduct'

    template_name = 'product/create_product.html'
    form_class = CreateProductForm
    success_url = reverse_lazy('catalog')


class EditProductView(PermissionRequiredMixin, auth_views.UpdateView):
    permission_required = 'web.add_abstractproduct'

    template_name = 'product/edit-product.html'
    form_class = EditProductForm
    queryset = AbstractProduct.objects.all()
    success_url = reverse_lazy('catalog')


class InfoProductView(LoginRequiredMixin, auth_views.DetailView):
    model = AbstractProduct
    template_name = 'product/ditailes-product.html'
    queryset = AbstractProduct.objects.all()


class DeleteProductView(auth_views.DeleteView, PermissionRequiredMixin):
    permission_required = 'web.delete_abstractproduct'

    model = AbstractProduct
    template_name = 'product/delete-product.html'
    queryset = AbstractProduct.objects.all()
    form_class = DeleteProductForm
    success_url = reverse_lazy('catalog')


class CatalogView(LoginRequiredMixin, auth_views.ListView):
    model = AbstractProduct
    template_name = 'product/catalog.html'
    context_object_name = 'objects'

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        if self.request.user.has_perm('web.delete_abstractproduct'):
            result['permission_required'] = True
        return result


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


# class CreateCartView(LoginRequiredMixin, auth_views.CreateView):
#     form_class = CreateCart
#     template_name = 'cart.html'
#     success_url = reverse_lazy('catalog')
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         form.instance.product = AbstractProduct.objects.get(pk=self.kwargs['pk'])
#
#         result = super().form_valid(form)
#
#         return result
def by_product(request, pk):
    product = AbstractProduct.objects.get(pk=pk)
    user = request.user
    Cart.objects.create(user=user, product=product)
    return redirect('catalog')


class PurchaseView(LoginRequiredMixin, auth_views.ListView):
    model = Cart
    template_name = 'purchase/purchase.html'

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        product_objects = Cart.objects.filter(user_id=self.request.user)
        result['products'] = product_objects
        result['total_money'] = sum([x.product.price for x in product_objects])
        return result


class ClearPurchaseTable(LoginRequiredMixin, DeleteView):
    model = Cart
    template_name = 'purchase/clear-purchase.html'
    queryset = Cart.objects.all()
    form_class = ClearProductsUser
    success_url = reverse_lazy('catalog')

# xxx
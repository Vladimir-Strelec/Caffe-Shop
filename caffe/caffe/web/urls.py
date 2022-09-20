from django.urls import path

from caffe.web.views import HomeTemplateView, CatalogView, CreateProductView, EditProductView, InfoProductView, \
    DeleteProductView, AllCommentsView, AddComments, PurchaseView, ClearPurchaseTable, by_product

urlpatterns = (
    path('', HomeTemplateView.as_view(), name='index'),

    path('catalog/', CatalogView.as_view(), name='catalog'),

    path('create/product/', CreateProductView.as_view(), name='create product'),
    path('edit/product/<int:pk>/', EditProductView.as_view(), name='edit product'),
    path('ditailes/product/<int:pk>/', InfoProductView.as_view(), name='info product'),
    path('delete/product/<int:pk>/', DeleteProductView.as_view(), name='delete product'),
    path('add/comment/product/<int:pk>/', AddComments.as_view(), name='add comment'),
    path('comments/view/product/<int:pk>/', AllCommentsView.as_view(), name='all comment'),

    path('cart/view/product/<int:pk>/', by_product, name='cart'),
    # path('cart/view/product/<int:pk>/', CreateCartView.as_view(), name='cart'),
    path('cart/view/purchase/<int:pk>/', PurchaseView.as_view(), name='purchase'),
    path('cart/view/purchase/clear/<int:pk>/', ClearPurchaseTable.as_view(), name='clear purchase'),

)

from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from caffe.accounts.views import UserLoginView, UserRegisterView, ProfileDetailsView, EditProfileView, \
    DeleteProfileView, ChangeUserPasswordView, LogOutUser

urlpatterns = (

    path('login/profile/', UserLoginView.as_view(), name='login user'),
    path('register/user/', UserRegisterView.as_view(), name='register'),
    path('detailes/<slug:pk>', ProfileDetailsView.as_view(), name='profile details'),
    path('profile/edit/<int:pk>', EditProfileView.as_view(), name='edit profile'),
    path('delete/profile/<int:pk>', DeleteProfileView.as_view(), name='profile delete'),


    path('edit-password/<int:pk>/', ChangeUserPasswordView.as_view(), name='change password'),
    path('logout/<int:pk>/', LogOutUser.as_view(), name='logout'),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('catalog')), name='password_change_done'),

    # path('profile/delete/', delete_profile, name='delete profile'),
)

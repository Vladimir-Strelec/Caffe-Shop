from django.contrib.auth import mixins as auth_mixin
from django.views import generic as views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from caffe.accounts.forms import CreateProfileForm, EditProfileForm
from caffe.accounts.models import Profile, ShopUser
from common.view_mixin import RedirectToCatalog


class UserRegisterView(RedirectToCatalog, views.CreateView):
    form_class = CreateProfileForm
    template_name = 'account/registration.html'
    success_url = reverse_lazy('login user')

    def form_valid(self, form):
        result = super().form_valid(form)
        Profile.objects.create(
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            user=self.object,
        )
        return result


class UserLoginView(auth_views.LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class EditProfileView(auth_mixin.LoginRequiredMixin, views.UpdateView):
    form_class = EditProfileForm
    template_name = 'account/edit-profile.html'
    success_url = reverse_lazy('index')
    queryset = Profile.objects.all()


class ProfileDetailsView(auth_mixin.LoginRequiredMixin, views.DeleteView):
    template_name = 'account/profile-details.html'
    queryset = Profile.objects.all()


class ChangeUserPasswordView(auth_mixin.LoginRequiredMixin, auth_views.PasswordChangeView):
    template_name = 'account/change-password.html'


class DeleteProfileView(auth_mixin.LoginRequiredMixin, views.DeleteView):
    model = ShopUser
    template_name = 'account/delete-profile.html'
    success_url = reverse_lazy('index')


class LogOutUser(auth_mixin.LoginRequiredMixin, auth_views.LogoutView):
    template_name = 'account/login.html'

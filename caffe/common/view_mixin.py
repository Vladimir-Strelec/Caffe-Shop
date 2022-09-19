from django.shortcuts import redirect


class RedirectToCatalog:

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('catalog')
        return super().dispatch(request, *args, **kwargs)
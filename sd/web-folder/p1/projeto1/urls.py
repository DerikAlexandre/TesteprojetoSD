from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/objetos/novo/', permanent=False)),
    path('', include('enquetes.urls')),
    path('admin/', admin.site.urls),
]

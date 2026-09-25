from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from apps.pages.views import index, catalog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index-page"),
    path('catalog/', catalog, name="catalog-page")
]
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
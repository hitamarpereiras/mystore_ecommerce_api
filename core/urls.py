from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.authentication.urls')),
    path('api/v1/', include('apps.accounts.urls')),
    path('api/v1/', include('apps.stores.urls')),
    path('api/v1/', include('apps.categories.urls')),
]

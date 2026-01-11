"""
URL configuration for inventory_pos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('inventory:dashboard'), name='home'),
    # path('accounts/', include('accounts.urls')),  # Removed: accounts app deleted
    path('inventory/', include('inventory.urls')),
    path('pos/', include('pos.urls')),
]

from django.core.exceptions import ImproperlyConfigured
try:
    # If using S3, MEDIA_URL will be an https URL
    if settings.MEDIA_URL.startswith('http'):
        pass  # Do not serve media locally
    else:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
except (AttributeError, ImproperlyConfigured):
    pass
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    
    # Add django-browser-reload for development
    # urlpatterns += [
    #     path('__reload__/', include('django_browser_reload.urls')),
    # ]

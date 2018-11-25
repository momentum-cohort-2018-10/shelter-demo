"""shelter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from pets import views as pets_views
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pets_views.index, name="dog_list"),
    path('contact/', pets_views.contact),
    path('dogs/<int:dog_id>/', pets_views.dog, name="dog_detail"),
    path(
        'dogs/<int:dog_id>/adopt/',
        pets_views.create_application,
        name="dog_application_detail"),
    path(
        'volunteer/',
        core_views.volunteer_application,
        name="volunteer_application",
    ),
    path(
        'accounts/register/',
        core_views.register,
        name="register",
    ),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

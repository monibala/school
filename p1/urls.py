"""p1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django import views
from django.conf import settings
from django.contrib import admin
from django.urls import path

"""p1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls.static import static

from myapp import views
from dashboard import views
from django.conf import settings



urlpatterns = [
    
    path('admin/', admin.site.urls),
    
    path('', views.home, name='home'),
    
    
    path('myapp/', include('myapp.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('contacts/', views.contact_view, name='contacts'),
    path('password_reset_confirm/<token>/<uidb64>', views.PasswordResetconfirm, name='password_reset_confirm'),
    path('recover-password/', views.recoverpassword, name='recover-password'),
    # path('recover-password/', views.password_reset_request, name='recover-password'),
    path('',include('payapp.urls')),
    path('paypalpay/',include('paypalpay.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('rpayapp/', include('rpayapp.urls')),
    
]
if settings.DEBUG:
    urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)


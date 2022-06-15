from myapp import views
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static


urlpatterns = [
    path('about/', views.about, name='about'),
    path('class/', views.classes, name = 'class'),
    path('teachers/', views.teachers, name = 'teachers'),
    path('gallery/', views.gallery, name = 'gallery'),
    path('contact/', views.contact, name = 'contact'),
    path('blog/', views.blog, name='blog'),
    path('single/', views.single, name='single'),
    path('check/', views.check, name='check'),
    path('delete_product/',views.delete_product, name='delete_product'),
    path('increment/',views.increment, name='increment'),
    path('decrement/',views.decrement, name='decrement'),
    path('checkout/',views.checkout, name='checkout'),
    path('cod/', views.cod, name='cod'),
    
]
if settings.DEBUG:
    urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)

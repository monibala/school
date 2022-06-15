from django.shortcuts import render
from dashboard import views
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    # path('', views.admin_dashboard, name='first'),
    path('', views.login, name='login'),
    # path('first', views.first, name='first'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    # path('recover-password/', views.password_reset_request, name='recover-password'),
    path('recover-password/', views.recoverpassword, name='recover-password'),
    path('index3/', views.administrator, name='index3'),
    path('calendar/', views.calendar_view,name='calendar'),
    path('mailbox/', views.mailbox, name='mailbox'),
    path('compose/', views.compose, name='compose'),
    # path('forgot-password', views.forgotpassword, name='forgot-password'),
    path('simple-results/', views.search_view, name='simple-results'),
    path('admin_starter/', views.starter_view, name='admin_starter'),
    path('simple/', views.tables_view, name='simple'),
    path('data/', views.table_data_view, name='data'),
    path('profile/', views.profile, name='profile'),
    # path('students/', views.students, name='students'),
    path('classes/', views.classes, name='classes'),
    # path('classes/', views.edit_classes, name='classes'),
    path('invoice/', views.invoice, name='invoice'),
    path('contacts/', views.contact_view, name='contacts'),
    path('contact-us', views.contactus_view, name='contact-us'),
    path('faq/', views.faq_view, name='faq'),
    path('reset-done/', views.resetdone, name = 'reset-done'),
    path('password_reset_confirm/<token>/<uidb64>', views.PasswordResetconfirm, name='password_reset_confirm'),
    path('reset-complete/', views.PasswordResetCompleteView, name='reset-complete'),
    # path('reset-done/', views.resetdone, name = 'reset-done'),
    # path('password_reset_confirm/<token>/', views.PasswordResetconfirm, name='password_reset_confirm'),
    # path('reset-complete/', views.PasswordResetCompleteView, name='reset-complete'),
    path('profile/', views.edit_profile, name='edit_profile'),
   
    # path('profile/', views.change_password, name='profile')
]
if settings.DEBUG:
    urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)

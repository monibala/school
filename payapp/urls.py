from .views import initiate_payment, callback
from django.urls import path
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('pay/', initiate_payment, name='pay'),
    path('payments/callback/', callback),
    path('login/', LoginView.as_view(), name='login'),
]
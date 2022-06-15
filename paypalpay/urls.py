from .views import initiate_payment
from django.urls import path

urlpatterns = [
    path('paypal/', initiate_payment, name='paypal'),
    # path('payment_done/',payment_done, name='payment_done'),
    # path('payment_canceled/', payment_canceled, name='payment_canceled'),
    
    
]
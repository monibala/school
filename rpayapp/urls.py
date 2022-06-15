from django.urls import path

# from .views import payment,payment_status
from .views import payment,payment_status
urlpatterns = [
    # path('rpay/',payment,name="rpay"),
    # path('order_summary/', payment_status,name="order_summary"),
    path('payment', payment, name='payment'),
    path('payment_status' , payment_status , name='payment_status')
]


from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.shortcuts import render

from myapp.models import Order
from myapp.models import OrderItem

from django.contrib.auth import authenticate, login as auth_login

from django.views.decorators.csrf import csrf_protect
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm

# Create your views here.

def initiate_payment(request):
    # order_id = request.session.get('orderid')
    # print(order_id)
    order = get_object_or_404(OrderItem)
    # order = Order.objects.get(user=User.objects.get(id=request.user.id))
    print(order)
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount' : order.total,
        # 'amount': '%.2f' % order.total().quantize(
        #     Decimal('.01')),
        # 'item_name': 'Order {}'.format(order.id),
        # 'invoice': str(order.id),
        # 'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        # 'return_url': 'http://{}{}'.format(host,
        #                                    reverse('payments/payment_done')),
        # 'cancel_return': 'http://{}{}'.format(host,
        #                                       reverse('payment_cancelled')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'payments/paypal.html', { 'form': form})
# def payment_done(request):
#     return render(request, 'payments/payment_done.html')



# def payment_canceled(request):
#     return render(request, 'payments/payment_cancelled.html')


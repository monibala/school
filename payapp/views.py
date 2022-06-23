from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.shortcuts import render

from myapp.models import Order
from payapp import paytm
from .models import Transaction
from django.contrib.auth import authenticate, login as auth_login
from .paytm import generate_checksum, verify_checksum
from django.views.decorators.csrf import csrf_protect
# Create your views here.

def initiate_payment(request):
    if request.method == "GET":
        return render(request, 'pay.html')
    try:
        username = request.POST['username']
        password = request.POST['password']
        amount = int(request.POST['amount'])
        user = authenticate(request, username=username, password=password)
        if user is None:
            raise ValueError
        auth_login(request=request, user=user)
    except:
        return render(request, 'pay.html', context={'error': 'Wrong Accound Details or amount'})
    order_id = paytm.__id_generator__()
    transaction = Transaction.objects.create(made_by=user, amount=amount, order_id=order_id)
    
    merchant_key = settings.PAYTM_SECRET_KEY
    
    params = (
        ('MID', settings.PAYTM_MERCHANT_ID),
        ('ORDER_ID', order_id),
        ('TXN_AMOUNT', str(transaction.amount)),
        ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
        ('WEBSITE', settings.PAYTM_WEBSITE),
        ('CUST_ID', str(transaction.made_by.email)),
        ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
        ('CALLBACK_URL', 'http://127.0.0.1:8000/callback/'),
        # ('PAYMENT_MODE_ONLY', 'NO'),
    )

    paytm_params = dict(params)
    checksum = generate_checksum(paytm_params, merchant_key)
   
    transaction.checksum = checksum
    transaction.save()
    
    paytm_params['CHECKSUMHASH'] = checksum
    print('SENT: ', checksum)
    print(paytm_params)
    
    return render(request, 'redirect.html',context=paytm_params)

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt    

def callback(request):
    if request.method == 'POST':
        received_data = dict(request.POST)
        paytm_params = {}
        paytm_checksum = received_data['CHECKSUMHASH'][0]
        for key, value in received_data.items():
            if key == 'CHECKSUMHASH':
                paytm_checksum = value[0]
            else:
                paytm_params[key] = str(value[0])
        # Verify checksum
        is_valid_checksum = verify_checksum(paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum))
        if is_valid_checksum:
            received_data['message'] = "Checksum Matched"
        else:
            received_data['message'] = "Checksum Mismatched"
            return render(request, 'callback.html', context=received_data)
        return render(request, 'callback.html', context=received_data)
        


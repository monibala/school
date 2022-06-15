from django.shortcuts import get_object_or_404, render
import razorpay
from django.views.decorators.csrf import csrf_exempt

from myapp.models import OrderItem


def payment(request):
    order = get_object_or_404(OrderItem)
    # amount = order.total
    print(order)
    # if request.method == "POST":
        
        # amount = amount
        # print(amount)
    client = razorpay.Client(auth=("rzp_test_1vDelUfydoNmf0", "FJ4lcy6BkkUhA6mx0MqWYc6n"))
    print(client)
    payment = client.order.create({'amount': 100, 'currency': 'INR','payment_capture': '1'})
    print(payment)
    order_id = payment['id']
    order_status = payment['status']
    context = {}
    context['order_id'] = payment['id']
    print(context)
#         if order_status=='created' :
# # Server data for user convinience
#             context [ ' product_id' ] = product
#             context[ 'price' ] = order_amount

#             context [ ' name' ] = name
#             context [ ' phone ' ] = phone
#             context [ ' email' ] = email

#             # data that'll be send to the razorpay for
#             context[' order_id' ] = order_id
    return render (request, 'payment.html',context)


    # return render(request, 'payment.html')

def payment_status(request):
    client = razorpay.Client(auth=("rzp_test_1vDelUfydoNmf0", "FJ4lcy6BkkUhA6mx0MqWYc6n"))
    response = request.POST

    params_dict = {
        'razorpay_payment_id' : response['razorpay_payment_id'],
        'razorpay_order_id' : response['razorpay_order_id'],
        'razorpay_signature' : response['razorpay_signature']
    }

    print(params_dict)
    # VERIFYING SIGNATURE
    try:
        status = client.utility.verify_payment_signature(params_dict)
        return render(request, 'order_summary.html', {'status': 'Payment Successful'})
    except:
        return render(request, 'order_summary.html', {'status': 'Payment Faliure!!!'})
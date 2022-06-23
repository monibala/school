
from pyexpat.errors import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render,get_object_or_404

# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render


from .models import Classes, Order, Checkout, OrderItem



# from .forms import bookingform

# Create your views here.

def home(request):
    # category_data = Category.objects.all()
    return render(request,'index.html')



def about(request):
    
    
    return render(request, 'about.html')

def classes(request):
    data = Classes.objects.all()
    return render(request, 'class.html', {'data':data})

def check (request):
    # del_id = request.GET.get('id')
    # print(del_id)
    prod = request.GET.get('product')
    user = User.objects.get(id=request.user.id)

    check_product = Order.objects.filter(id=prod,user=user)
    
    quantity = 0
    if prod!=None:
        if(len(check_product)>0) :
            order_prod = check_product[0]
            order_prod.quantity+=1
            order_prod.save()
        else:
            check_products, created=Order.objects.get_or_create(user=User.objects.get(id=request.user.id),productid=prod)
            # check_products=Order(user=User.objects.get(id=request.user.id),productid=prod)
            # check_products.save()
       
           
        check_products = Order.objects.filter(user=User.objects.get(id=request.user.id))
        
        li = []
        subtotal = 0
        total = 0
        
        for i in check_products:
            products = Classes.objects.filter(id=i.productid)
            prod = Classes.objects.get(id=i.productid)
            subtotal =int(prod.fee)*i.quantity
            li.append([products,subtotal,i.quantity])
        
            total = int(total) + int(subtotal)
            # crt = Order(name=prod.name,fee=prod.fee,total=total,user=user,subtotal=subtotal,quantity=quantity)
            # crt.save()
            crt = OrderItem(total=total)    
            crt.save()       
  
       
        res = {'data':li, 'total':total}
        print(res)
        return render(request,'check.html',res)
        
    return render(request,'check.html')

def delete_product(request):
    del_id = request.GET.get('id')
    print(del_id)
    prod = request.GET.get('product')
    user = User.objects.get(id=request.user.id)
    check_product = Order.objects.filter(id=prod,user=user)
    if del_id!=None:
    
        del_order = Classes.objects.get(id=del_id) 
        del_prod = Order.objects.filter(productid=del_id,user = user)
        print(del_prod)
        del_prod.delete()
    check_products = Order.objects.filter(user=User.objects.get(id=request.user.id))
        
    li = []
    subtotal = 0
    total = 0
        
    for i in check_products:
        products = Classes.objects.filter(id=i.productid)
        prod = Classes.objects.get(id=i.productid)
        subtotal =int(prod.fee)*i.quantity
        li.append([products,subtotal,i.quantity])
        
        total = int(total) + int(subtotal)
    res = {'data':li, 'total':total}
    return render(request,'check.html',res)  
    
    
   

# def increment(request):
#     incr_id = request.GET.get('incrid')
#     decr_id = request.GET.get('decrid')
#     # decr_id = request.GET.get('decrid')
#     user = User.objects.get(id=request.user.id)
#     print(incr_id)
#     print(user)
    
#     prod = Order.objects.filter(productid=incr_id,user=user)
#     prod1 = Order.objects.filter(productid=decr_id,user=user)
#     print(prod)

#     if prod!=None:
#         # print(prod,'//')
#         if len(prod)>0:
#             ob=prod[0]
#             ob.quantity+=1
#             ob.save()
#     elif prod1!=None:
#         if len(prod1)>0:
#             ob=prod1[0]
#             ob.quantity-=1
#             ob.save()
#     else: 
#         crts=Order(user=User.objects.get(id=request.user.id),productid=prod,quantity=1)
#         crts.save()
   
        
   
#     return redirect("check")
def decrement(request):
    
    
    decr_id = request.GET.get('decrid')
    user = User.objects.get(id=request.user.id)
    print(decr_id)
    print(user)
    
    prod = Order.objects.get(productid=decr_id,user=user)
    print(prod)

    if (prod.quantity - 1)> 0:
        prod.quantity-=1
        prod.save()
    check_products = Order.objects.filter(user=User.objects.get(id=request.user.id))
        
    li = []
    subtotal = 0
    total = 0
        
    for i in check_products:
        products = Classes.objects.filter(id=i.productid)
        prod = Classes.objects.get(id=i.productid)
        subtotal =int(prod.fee)*i.quantity
        li.append([products,subtotal,i.quantity])
        
        total = int(total) + int(subtotal)
    res = {'data':li, 'total':total}
    return render(request,'check.html',res)

def increment(request):
    incr_id = request.GET.get('incrid')
    user = User.objects.get(id=request.user.id)
    print(incr_id)
    print(user)
    
    prod = Order.objects.get(productid=incr_id,user=user)
    print(prod)

    if (prod.quantity +1)> 0:
        prod.quantity+=1
        prod.save()
    check_products = Order.objects.filter(user=User.objects.get(id=request.user.id))
    crt = Order(quantity=prod.quantity)    
    crt.save()
    li = []
    subtotal = 0
    total = 0
        
    for i in check_products:
        products = Classes.objects.filter(id=i.productid)
        prod = Classes.objects.get(id=i.productid)
        subtotal =int(prod.fee)*i.quantity
        li.append([products,subtotal,i.quantity])
        
        total = int(total) + int(subtotal)
    res = {'data':li, 'total':total}
    return render(request,'check.html',res)
def checkout(request):
    user = User.objects.get(id=request.user.id)
    check_products = Order.objects.filter(user=User.objects.get(id=request.user.id))
 
    li = []
    subtotal = 0
    total = 0
        
    for i in check_products:
        products = Classes.objects.filter(id=i.productid)
        prod = Classes.objects.get(id=i.productid)
        subtotal =int(prod.fee)*i.quantity
        li.append([products,subtotal,i.quantity])
        
        total = int(total) + int(subtotal)
    res = {'data':li, 'total':total}

    # Form 
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        mob_no=request.POST.get('mob_no')
        Address=request.POST.get('Address')
        State = request.POST.get('State')
        pincode = request.POST.get('pincode')

        check = Checkout(user = User.objects.get(id=request.user.id), fname=fname,lname=lname,email=email,mob_no=mob_no,Address=Address,State=State,pincode=pincode)
        print(check)
        check_products = Order.objects.filter(user=User.objects.get(id=request.user.id))
        check_products.delete()
        check.save()
        return redirect('pay')

    return render(request, 'checkout.html',res)
def teachers(request):
    return render(request,  'team.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def single(request):
    return render(request, 'single.html')

def cod(request):
    return render(request, 'cod.html')

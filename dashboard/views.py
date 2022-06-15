from msilib.schema import Class
from sre_constants import SUCCESS
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
# Create your views here.
from email import message
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.http import BadHeaderError, HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib import messages 
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.http  import urlsafe_base64_decode, urlsafe_base64_encode
from django.db.models.query_utils import Q
from django.contrib import messages
from django.utils.encoding import force_str
from django.contrib.auth import get_user_model, update_session_auth_hash
from myapp.models import Classes
from .models import Profile, contact
from .forms import  NewUserForm, PasswordResetRequestForm, SetPasswordForm, UpdateClassForm, UpdateProfileForm, adminform
from django.utils.decorators import method_decorator
from django.forms import Form, ValidationError
from django.template import loader



# Create your views here.
def home (request):
    return render(request,'index.html')


# def admin_dashboard(request):
#     return render (request, 'first.html')

def login(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # login(request, user)
            return render(request, 'index3.html')

        else:
            messages.info(request, 'Username or Password is incorrect!')
        
    template = 'login.html'
    context = {}
    return render(request, template, context)
def logout(request):
    if request.method == 'POST':
        logout(request)
    return redirect('login')

  
def register(request):
    form = NewUserForm()
    if request.method == 'POST':

        form = NewUserForm(request.POST)
        if form.is_valid():

            form.save()
            
            
            return redirect('login')

    else:
        form = NewUserForm()

    return render(request, 'register.html', {'form': form })

    
def administrator(request):
    
    return render(request, 'index3.html')

def mailbox(request):
    return render(request,'mailbox.html')

def compose(request):
    return render(request,'compose.html')
# def forgotpassword(request):
#     return render(request,'forgot-password.html')

def recoverpassword(request):
    if request.method == "POST":
        form = PasswordResetRequestForm(request.POST)
     
        if form.is_valid():
        #     print(form)
        # else:
            data = request.POST.get('email')
            print(data)
            user = User.objects.filter(Q(email=data)).first()
            print(user)
            if user:
                c = {
                "email":user.email,
                'domain':'127.0.0.1:8000',
                'site_name': 'Website',
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "user": user,
                'token': default_token_generator.make_token(user),
                'protocol': 'http',
                }
                print(c)
                email_template_name='registration/password_reset_email.html'
                subject = "Reset Your Password"
                email = loader.render_to_string(email_template_name, c)
                send_mail(subject, email,'smonicse@gmail.com' , [user.email], fail_silently=False)
            messages.success(request, 'An email has been sent to ' + data +" ")
                
        return render(request, 'recover-password.html', context={"form":form})

def resetdone(request):
    return render(request,'reset-done.html')
def PasswordResetconfirm(request, token, uidb64):
    form = SetPasswordForm(request.POST)
    UserModel = get_user_model()
    try:
        uid = urlsafe_base64_decode(uidb64)
        user = User._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

        if user is not None and default_token_generator.check_token(user, token):
            new_password= form.cleaned_data['new_password2']
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Password reset has been successful.')
        else:
            messages.error(request, 'Password reset has not been unsuccessful.')
        # return form
    return render (request,'password_reset_confirm.html',{'form':form})    
def PasswordResetCompleteView(request):
    return render(request, 'reset-complete')
 


def calendar_view(request):
    return render(request, 'calendar.html')

def starter_view(request):
    return render (request, 'admin_starter.html')

def search_view(request):
    return render(request,'simple-results.html')
def tables_view(request):
    return render(request,'simple.html')

def table_data_view(request):
    return render(request,'data.html')

def invoice(request):
    return render(request,'invoice.html')



def profile(request):
    profile_data = Profile.objects.all()
    profile_id = Profile.objects.filter(id=request.POST.get('edit')).first()
    # print(profile_id)
    profile_form = UpdateProfileForm(request.POST,instance=profile_id)
    if profile_form.is_valid():
        profile_form.save()
        return redirect('profile')

    
# Change Password
  
    if request.method == 'POST':
        id = request.POST.get('user')
        form = adminform( request.POST)
        if form.is_valid():
            old_password = request.POST['old_password']
            new_password = request.POST['new_password']
            profile_id = User.objects.filter(id=id).first()
            print(profile_id)
            password = make_password(new_password, salt=None, hasher='default')
            profile_id.password=password
            
            print(profile_id.password)
            profile_id.save()
            
        else:
            messages.error(request, 'Please correct the error below.')
        
    else:
        form = adminform(request.user)
    return render (request, 'profile.html',{'profile_data':profile_data})
    
    
def edit_profile(request):
    return render(request, 'profile.html')
    
def classes(request):
    data = Classes.objects.all()  
    dl = request.POST.get('delete')
    edit = request.POST.get('edit')
    if request.method=="POST":
        if dl!=None:    
            obj = Classes.objects.filter(id=dl)
            obj.delete()
        elif edit!=None:
            name = request.POST.get('name')
            age = request.POST.get('age')
            description = request.POST.get('description')
            fee = request.POST.get('fee')
            seats = request.POST.get('seats')
            images = request.POST.get('images')
            time = request.POST.get('time')
            prod= Classes.objects.filter(id = edit)
            if len(prod)>0:
                ob=prod[0] 
                print(ob)
                if len(name)>0:
                    print(name)
                    ob.name=name
                if len(age)>0:
                    print(age)
                    ob.age=age
                if len(description)>0:
                    print(description)
                    ob.description=description
                if len(fee)>0:
                    ob.fee=fee 
                if len(seats)>0:
                    ob.seats=seats
                if len(time)>0:
                    ob.time=time
                if images:       
                    ob.images=images
                ob.save()
                return redirect('classes') 
        else:
            name=request.POST['name']
            age=request.POST['age']
            seats=request.POST['seats']
            fee=request.POST['fee']
            description=request.POST['description']
            time=request.POST['time']
            images=request.FILES['images']
            add_data = Classes(name=name,age=age,seats=seats,description=description,time=time,fee=fee,images=images)
            add_data.save()
    
                                                            
    return render(request,'classes.html', {'data':data}) 
    
  

def contact_view(request):
    if request.method == "POST":
        Name = request.POST['Name']
        Email = request.POST['Email']
        Mobile_Number = request.POST['Mobile_Number']
        Message = request.POST['Message']
        con = contact(Name=Name,Email=Email,Mobile_Number=Mobile_Number,Message=Message)
        con.save()
        send_mail(Name,Message,Mobile_Number,['smonicse@gmail.com'],['Email'])
        print(Name)
        print(send_mail)
    return render(request,'contacts.html')
def contactus_view(request):
    return render(request, 'contact-us.html')
def faq_view(request):
    return render(request,'faq.html')


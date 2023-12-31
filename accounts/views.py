from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Profile

# Create your views here.
def login_page(request):
    if request.method=='POST':        
        U_name=request.POST.get('usrname')
        Pswrd=request.POST.get('pswrd')
        usr_obj=User.objects.filter(username = U_name)
        if not usr_obj.exists():    
            messages.warning(request, "Account not exist.")
            if not usr_obj[0].profile.is_verified:
                messages.warning(request, "Email is not verified")
                return HttpResponseRedirect(request.path_info)
            return HttpResponseRedirect(request.path_info)
        
        usr_obj=authenticate(username=U_name,password=Pswrd)
        if usr_obj:
            login(request, usr_obj)
            return redirect('/')

        messages.error(request, "Password is not correct")
        return HttpResponseRedirect(request.path_info)


    return render (request, 'accounts/login.html')
    
def user_regs (request):
    if request.method=='POST':
        f_name=request.POST.get('F_Name')
        l_name=request.POST.get('L_Name')
        email=request.POST.get('e_mail')
        paswrd=request.POST.get('pass')
        usr_obj=User.objects.filter(username = email)
        if usr_obj.exists():    
            messages.warning(request, "Profile already exists.")
            return HttpResponseRedirect(request.path_info)
        usr_obj=User.objects.create(first_name=f_name, last_name=l_name, email=email, username=email)
        usr_obj.set_password(paswrd)
        usr_obj.save()
        messages.success(request, "Profile is created sucessfully__")
        return HttpResponseRedirect(request.path_info)
    return render (request, 'accounts/register.html')


def accont_activation(request, email_token):
    try:
        usr_obj=Profile.objects.get(email_token=email_token)
        usr_obj.is_verified=True
        usr_obj.save()
        messages.success(request, "Account is verified,Please LogIn")
        return redirect('LogIn')
    except Exception as e:
        return HttpResponse("Invalid token please recheck")
    
def logout_view(request):
    logout(request)
    return redirect('/')




def profile(request):
    user=request.user
    details=Profile.objects.get(user=user)
    if request.method=='POST':
        details.contact_no=request.POST.get('mynumber')
        details.gender=request.POST.get('add_gender')
        details.address=request.POST.get('add_address')
        details.save()
        return HttpResponseRedirect(request.path_info)
        
    return render (request, 'accounts/profile.html',{'user':user,'details':details})

def add_img(request):
    user=request.user
    details=Profile.objects.get(user=user)
    if request.method=='POST':
        details.profile_image=request.FILES.get('myImage')
        details.save()
        return redirect('Profile')
    return redirect('Profile')
    





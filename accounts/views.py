from django.shortcuts import render,redirect
from .forms import CustomerSignupForm,LoginForm,EditProfileForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

# Create your views here.
def customer_signup(request):
    if request.method == 'POST':
        form = CustomerSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = CustomerSignupForm()
    return render(request, 'accounts/customer_signup.html', {'form': form})



# login view
def login_view(request):
    if request.method =='POST':
        form =LoginForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print(f"User role is:{user.role}")
            login(request,user)
            return redirect_by_role(user)
    else:
        form = LoginForm()
    return render(request,'accounts/login.html',{'form':form})


def redirect_by_role(user):
    role  = getattr(user,'role','').strip().lower()
    print(f"User redirect role is:{role}")
    if role == 'admin':
        return redirect('admin_dashboard')  # Replace with your admin dashboard URL name
    elif role == 'staff':
        return redirect('staff_dashboard')  # Replace with your staff dashboard URL name
    else:
        return redirect('home')  # Default redirect for customers and other roles        
    
    
    

# logout view
def logout_view(request):
    logout(request)
    return redirect('home')


# edit profile view
def edit_profile(request):
    if request.method=='POST':
        print(type(request.POST))
        username = request.POST.get('username','').strip()
        print(f"Username from form: {username}")
        form = EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('edit_profile')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request,'accounts/edit_profile.html',{'form':form})
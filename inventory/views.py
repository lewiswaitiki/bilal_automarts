from django.shortcuts import render, redirect
from .models import Vehicle, VehicleImage
from .forms import VehicleForm, VehicleImageFormSet,VehicleInquiryForm
from django.contrib.auth.decorators import user_passes_test
from django.core.mail import send_mail
from django.contrib import messages


def is_admin(user):
    return user.is_authenticated and user.role =='admin'



# Homepage view
def home(request):
    return render(request, 'inventory/index.html')

# All vehicles listing view
# def vehicles(request):
#     vehicles = Vehicle.objects.filter(available=True)
#     return render(request, 'inventory/all_vehicles.html', {'vehicles': vehicles})


def vehicles(request):
    
    vehicles = Vehicle.objects.all()
    
    
    filters = {}
    
    for field in ['category','transmission', 'fuel_type','drive_type']:
        value = request.GET.get(field)
        if value:
            filters[f"{field}__iexact"]= value
            
    if filters:
        vehicles = vehicles.filter(**filters)
    

    
    

    return render(request, 'inventory/all_vehicles.html',{'vehicles':vehicles})




# Vehicle submission view
@user_passes_test(is_admin)
def submit_vehicle(request):
    if request.method == 'POST':
        vehicle_form = VehicleForm(request.POST, request.FILES)
        image_formset = VehicleImageFormSet(request.POST, request.FILES, queryset=VehicleImage.objects.none())

        if vehicle_form.is_valid() and image_formset.is_valid():
            vehicle = vehicle_form.save()

            for form in image_formset.cleaned_data:
                if form:
                    VehicleImage.objects.create(
                        vehicle=vehicle,
                        image=form['image'],
                        caption=form.get('caption', '')
                    )

            return redirect('vehicles')  # or 'home' or a success page
    else:
        vehicle_form = VehicleForm()
        image_formset = VehicleImageFormSet(queryset=VehicleImage.objects.none())

    return render(request, 'inventory/submit_vehicle.html', {
        'vehicle_form': vehicle_form,
        'image_formset': image_formset,
    })


def vehicle_detail(request, vehicle_id):
    vehicle = Vehicle.objects.get(id=vehicle_id)
    return render(request, 'inventory/vehicle_detail.html', {'vehicle': vehicle})


# admin dashboard view
@user_passes_test(is_admin)
def admin_dashboard(request):
    vehicles = Vehicle.objects.all()
    return render(request,'inventory/admin_dashboard.html',{'vehicles':vehicles})
    

#delete vehicle view
@user_passes_test(is_admin)
def delete_vehicle(request,vehicle_id):
    try:
        vehicle = Vehicle.objects.get(id=vehicle_id)
        vehicle.delete()
        messages.success(request, f"Vehicle '{vehicle.title}' was successfully deleted.")
    except Vehicle.DoesNotExist:
        messages.error(request, "Vehicle not found. Deletion failed.")
    return redirect('admin_dashboard')



# send inquiry view
def vehicle_inquiry(request,vehicle_id):
    vehicle = Vehicle.objects.get(id=vehicle_id)
    if request.method =='POST':
        form =VehicleInquiryForm(request.POST)
        if form.is_valid():
            # Process the inquiry (e.g., send email)
            try:
                send_mail(
                    subject=f"Inquiry about {vehicle.title}",
                    message=form.cleaned_data['message'],
                    from_email=form.cleaned_data['email'],
                    recipient_list=['lewiswaitiki9@gmail.com']
                )
                return redirect('vehicles')  # Redirect after successful submission/thank you page
            except Exception as e:
                # Handle the error (e.g., log it, show a message to the user)
                print(f"Error sending email: {e}")
        
    else:
        form = VehicleInquiryForm()
    return render(request,'inventory/vehicle_inquiry.html',{'form':form,'vehicle':vehicle})
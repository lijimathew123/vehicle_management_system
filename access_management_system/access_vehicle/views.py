from django.shortcuts import get_object_or_404, redirect, render
from .forms import UserRegistrationForm,VehicleUpdateForm,VehicleAddForm,AdminAddForm
from .models import User,Vehicle
from django.contrib.auth import logout


# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Automatically set the role to 'user'
            user = form.save(commit=False)
            user.role = 'user'
            user.save()
            # Redirect to the 'index.html' page
            return redirect('index')  
    else:
        form = UserRegistrationForm()
    
    return render(request, 'register.html', {'form': form})


# User login management
def login(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']

        try:
            # Retrieve the user from the database based on the username
            user = User.objects.get(username =username)

            if user.password == password:
                request.session['user_id']= user.id
                return redirect('vehicle_list')
            else:
                error_message = 'Invalid username or passowrd'
        except User.DoesNotExist:
            error_message = 'Invalid username or password'
    else:
        error_message=''

    return render(request,'index.html',{'error_message':error_message})


#Vehicle list display section

def vehicle_list(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        try:
             user= User.objects.get(id=user_id)
             vehicles = Vehicle.objects.all()

             return render(request, 'view_vehicle.html', {'vehicles':vehicles, 'user': user})

        except User.DoesNotExist:
            return redirect('index')
     
    return redirect('index') 
        



#update vehicle section

def update_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)

    if request.method == 'POST':
        form = VehicleUpdateForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')  # Redirect to the vehicle list page after successful update
    else:
        form = VehicleUpdateForm(instance=vehicle)

    return render(request, 'update_vehicle.html', {'form': form})

# Delete vehicle section

def delete_vehicle(request, vehicle_id):
    # Get the vehicle object to delete
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)

    if request.method == 'POST':
        # Confirm deletion (if needed)
        # Delete the vehicle
        vehicle.delete()
        return redirect('vehicle_list')  # Redirect to the vehicle list page after successful deletion

    return render(request, 'delete_vehicle.html', {'vehicle': vehicle})


#Add vehicle section

def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')  # Redirect to the vehicle list page after adding the vehicle
    else:
        form = VehicleAddForm()

    return render(request, 'add_vehicle.html', {'form': form})


#view all sub admins in the system
def admin_list(request):
    user = User.objects.filter(role='admin')
    return render(request,'admin_list.html',{'admin':user})

#Delete admin

def delete_admin(request,user_id):
    admin = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        admin.delete()
        return redirect('admin_list')
    return render(request, 'delete_admin.html',{'admin':admin})

#add admin section

def add_admin(request):
    if request.method == 'POST':
        form = AdminAddForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'admin'
            user.save()

            return redirect('admin_list')
    else:
        form = AdminAddForm()
    return render(request,'add_admin.html',{'form':form})



#logout profile
def user_logout(request):
    logout(request)
    return redirect('index')






from django.shortcuts import render, HttpResponse
from django.contrib import messages
from users.models import UserRegistrationModel

# Create your views here.

# Admin Login Check
def AdminLoginCheck(request):
    if request.method == 'POST':
        usrid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')
        print("User ID is = ", usrid)
        if usrid == 'admin' and pswd == 'admin':
            return render(request, 'admins/AdminHome.html')
        else:
            messages.success(request, 'Please Check Your Login Details')
    return render(request, 'AdminLogin.html', {})


# Admin Home
def AdminHome(request):
    return render(request, 'admins/AdminHome.html')


# View Registered Users
def RegisterUsersView(request):
    data = UserRegistrationModel.objects.all()
    return render(request, 'admins/viewregisterusers.html', {'data': data})


# Activate User Status
def ActivaUsers(request):
    if request.method == 'GET':
        id = request.GET.get('uid')
        status = 'activated'
        print("PID = ", id, status)
        UserRegistrationModel.objects.filter(id=id).update(status=status)
        data = UserRegistrationModel.objects.all()
        return render(request, 'admins/viewregisterusers.html', {'data': data})


# Delete User
def DeleteUsers(request):
    if request.method == 'GET':
        id = request.GET.get('uid')  # Fetch the user ID from the URL
        print("Deleting user with ID:", id)
        
        # Deleting the user
        UserRegistrationModel.objects.filter(id=id).delete()

        # After deletion, fetch all remaining users to display on the page
        data = UserRegistrationModel.objects.all()
        
        # Render the page to show the updated list of users
        return render(request, 'admins/viewregisterusers.html', {'data': data})

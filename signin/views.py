# from django.shortcuts import render
# from django.contrib.auth import logout,login,authenticate
# from .models import besant
# from django.http import HttpResponse
# # Create your views here.
# def home(request):
#     #return HttpResponse("Welcome to homepage")
#     return render(request,'home.html')


# # def signup(request):
# #     if request.method == 'POST':
# #         username = request.POST['username']
# #         email = request.POST['email']
# #         password = request.POST['password']
# #         confirm_password = request.POST['confirm_password']

# #         print(f"Received data: {username}, {email}, {password}, {confirm_password}")

# #         if password != confirm_password:
# #             return HttpResponse("Passwords do not match")

# #         try:
# #             if User.objects.filter(username=username).exists():
# #                 return HttpResponse("Username already exists")
# #             if User.objects.filter(email=email).exists():
# #                 return HttpResponse("Email already registered")

# #             # Create the user
# #             user = User.objects.create_user(username=username, email=email, password=password)
# #             user.save()

# #             print("User created successfully.")
# #             return redirect('signin')
# #         except Exception as e:
# #             print(f"Error occurred: {str(e)}")
# #             return HttpResponse(f"An error occurred: {str(e)}")

# #     return render(request,'signup.html')


#     return render(request, "home.html")

# def signup(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']
#         besant.objects.create_user(username=username, password=password)
#         besant.save()
#     return render(request, 'signup.html')

# def signin(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             return HttpResponse("Invalid credentials")
#     return render(request, 'signin.html')

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout,login,authenticate
from .models import BesantUser

def home(request):
    return HttpResponse("Welcome to homepage")
    return render(request,'home.html')
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check if passwords match
        if password != confirm_password:
            return HttpResponse("Passwords do not match")

        # Check if username or email already exists
        if BesantUser.objects.filter(username=username).exists():
            return HttpResponse("Username already exists")
        if BesantUser.objects.filter(email=email).exists():
            return HttpResponse("Email already registered")

        # Create and save the user with plaintext password
        BesantUser.objects.create(username=username, email=email, password=password)

        return render(request,"signin.html")

    return render(request, 'signup.html')
    
# def signin(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST.get()['password']
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             return HttpResponse("Invalid credentials")
#     return render(request, 'signin.html')


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BesantUser

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        print(username,password)

        # Check if both fields are provided
        if not username or not password:
            return HttpResponse("Both username and password are required")

        # Validate the user
        try:
            user = BesantUser.objects.get(username=username, password=password)
            print(user)
            # Successful login
            return HttpResponse(f"Welcome, {user.username}! You are logged in.")
        except BesantUser.DoesNotExist:
            # Invalid credentials
            return HttpResponse("Invalid username or password")

    return render(request, 'signin.html')
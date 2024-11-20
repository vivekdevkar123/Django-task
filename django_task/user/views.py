from django.shortcuts import render,redirect
from django.contrib.auth import logout
# Create your views here.

def home(request):
    try:
        # Your existing code for the home view here
        return render(request, 'home.html')
    except Exception as e:
        print(f"Error: {e}")
        raise

def logout_view(request):
    logout(request)
    return redirect("/")
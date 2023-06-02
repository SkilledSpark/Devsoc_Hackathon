from django.shortcuts import render
from django.http import HttpResponseRedirect

def form_submission(request):
    if request.method == "POST":
        # Retrieve the username and password from the form
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Perform any necessary processing or storage of the username and password

        # Redirect to the analysis route
        return HttpResponseRedirect("/health/home/")
    else:
        return render(request, 'health/login.html')

def redirect(request):
    return render(request, "health/home.html")

def login(request):
    return HttpResponseRedirect("/health/login")

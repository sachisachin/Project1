from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse("You are now logged in.")
        else:
            return render(request, 'login/login.html', {'error_message': 'Invalid login credentials.'})

    return render(request, 'login/login.html')
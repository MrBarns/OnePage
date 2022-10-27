from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate


from .models import *
from .forms import *

# For feedback messages
from django.contrib import messages

def loginView(request):
    form = LoginForm()
    email = request.POST.get('email')
    password = request.POST.get('password')

    if request.method == 'POST':
        try:
            user = User.objects.get(email = email)
            
        except:
            messages.error(request, "User does not exist")
    
    user = authenticate(request, email = email, password = password)

    if user is not None:
        login(request, user)
        return redirect('fill_details')

    context = {'form': form}
    return render(request, 'login_page.html', context)

def logoutView(request):
    logout(request)
    return redirect('login')


def fillDetailsView(request):
    form = detailsForm()


    context = {'form': form}
    return render(request, 'fill_details.html', context)




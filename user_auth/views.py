
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate


from .models import *
from .forms import *

# For feedback messages
from django.contrib import messages

def registerView(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit = False)
            user.email = user.email.lower()
            user.save()

            login(request, user)
            return redirect('fill_details')

        else:
            messages.error(request, "Error occured during registration.\n \
            Please try again.")


    context = {'form': form}
    return render(request, 'registration.html', context)

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

    else:
        messages.error(request, "Incorrect username or password")

    context = {'form': form}
    return render(request, 'login_page.html', context)

def logoutView(request):
    logout(request)
    return redirect('login')


def fillDetailsView(request):
    form = detailsForm()


    context = {'form': form}
    return render(request, 'fill_details.html', context)




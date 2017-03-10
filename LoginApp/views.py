from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .forms import LoginForm


# Create your views here.

def user_login(request):

    if request.method == 'POST':

        form = LoginForm(request.POST)

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/dashboard/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            return HttpResponse("Invalid login details supplied.")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

@login_required
def dashboard(request):

    return render(request, 'dashboard.html')

@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/logout/')



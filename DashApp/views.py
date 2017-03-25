from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def dashboard(request):

	return render(request, 'dashboard.html')


def show_tsops(request):

	return render(request, 'tsops.html')


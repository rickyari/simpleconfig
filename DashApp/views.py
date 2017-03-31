from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.

@login_required
def dashboard(request):

	return render(request, 'dashboard.html')


@login_required
def show_tsops(request):

	return HttpResponseRedirect('http://10.187.100.188:8080/job/LinuxPatchJob/')
	
@login_required
def show_egencia(request):

	return render(request, 'egencia.html')


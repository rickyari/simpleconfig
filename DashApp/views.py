from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
import requests

# Create your views here.

@login_required
def dashboard(request):

	return render(request, 'dashboard.html')


@login_required
def show_tsops(request):

	return HttpResponseRedirect('https://drone.idx.expedmz.com/tsops/job/LinuxPatchJob')
	
@login_required
def show_egencia(request):

	return render(request, 'egencia.html')

def tsops_status(request):

	#url_api = "http://10.187.100.188:8080/job/LinuxPatchJob/lastBuild/api/json?tree=executor[progress]"
	#headers = {"Accept":"application/json"}
	#response = requests.get(url_api, headers=headers )

	#result = response.json()['executor']

	#if result != None:
	#	result_percent = str(result['progress']) + "%"
	#else:
	#	result_percent = "0" + "%"
		
	#return render(request, 'status.html', {'result': result_percent})
	return render(request, 'tsops_status.html')


def get_percent(request):

	url_api = "http://10.187.100.188:8080/job/LinuxPatchJob/lastBuild/api/json?tree=executor[progress]"
	headers = {"Accept":"application/json"}
	response = requests.get(url_api, headers=headers )

	result = response.json()['executor']

	if result != None:
		result_percent = str(result['progress']) + "%"
	else:
		result_percent = "0" + "%"

	data = {'percent': result_percent}
		
	return HttpResponse(result_percent)


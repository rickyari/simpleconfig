from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from .scripts import JenkinsApi
from .scripts import ServiceCriticality

# Create your views here.

@login_required
def dashboard(request):

	return render(request, 'dashboard.html')


@login_required
def show_tsops(request):

#	return HttpResponseRedirect('https://drone.idx.expedmz.com/tsops/job/LinuxPatchJob')
	return render(request, 'tsops.html')
	
@login_required
def show_egencia(request):

	return render(request, 'egencia.html')


def tsops_status(request):

	total_services = JenkinsApi.get_services()
	running_jobs = JenkinsApi.running_jobs()
	services_data = ServiceCriticality.get_criticality()
	progress_data = ServiceCriticality.CalculatePercent()
	
	return render(request, 'tsops_status.html',
	{'total_services': total_services, 
	'running_jobs': running_jobs,
	'services_data': services_data,
	'progress_data': progress_data}
	)


#def get_percent(request):

#	url_api = "http://10.187.100.188:8080/job/LinuxPatchJob/lastBuild/api/json?tree=executor[progress]"
#	headers = {"Accept":"application/json"}
#	response = requests.get(url_api, headers=headers )
#
#	result = response.json()['executor']
#
#	if result != None:
#		result_percent = str(result['progress']) + "%"
#	else:
#		result_percent = "0" + "%"
#
#	data = {'percent': result_percent}
#		
#	return HttpResponse(result_percent)



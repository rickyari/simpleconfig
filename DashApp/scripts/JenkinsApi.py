import requests

def get_services():

	# Get Total Services

	uri = "http://chexjvaord064:8500/v1/kv/?keys=true"
	response = requests.get(uri)

	services = set()
	for keys in response.json():
		key = keys.split('/')[0]
		services.add(key)
	
	lin_services = []
	for srv in services:
		srv_url = 'http://chexjvaord064:8500/v1/kv/%s/PROD/OS_TYPE?raw' % srv
		srv_response = requests.get(srv_url)
		os_type = srv_response.text
		if os_type == 'LINUX':
			lin_services.append(srv)
	
	total_services = lin_services
	
	return total_services
	
def running_jobs():

	# Get All The Running Jobs (LinuxPatchJob)
	
	jenkins_server = 'https://drone.idx.expedmz.com/tsops/'
	api_query = 'computer/api/json?tree=computer[executors[currentExecutable[url]],oneOffExecutors[currentExecutable[url]]]&xpath=//url&wrapper=builds'
	user = 'gagsingh'
	pwd = 'Dontask@123'
	
	uri = jenkins_server + api_query
	result = requests.get(uri, auth=(user, pwd), verify=False)
	
	running_jobs = []
	job_list = result.json()['computer']
	
	for i in job_list:
		jobs = i['executors']
		for x in jobs:
			if x['currentExecutable'] != None:
				if 'LinuxPatchJob' in x['currentExecutable']['url']:
					running_jobs.append(x['currentExecutable']['url'])
	
	return len(running_jobs)
	
	
	

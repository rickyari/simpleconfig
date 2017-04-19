import requests

def get_services():

	# Get Total Services

	uri = "http://chexjvaord064:8500/v1/kv/?keys=true"
	response = requests.get(uri)

	services = set()
	for keys in response.json():
		key = keys.split('/')[0]
		services.add(key)
	
	total_services = len(services)
	
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
				running_jobs.append(x['currentExecutable']['url'])
	
	return len(running_jobs)
	
	
	
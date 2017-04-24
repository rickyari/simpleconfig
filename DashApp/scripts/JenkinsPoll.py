#!/usr/bin/env python

import requests
from backlog import backlog

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
	
print  len(running_jobs)
print running_jobs


pending_jobs = backlog

if len(running_jobs) == 0:
	
	if len(pending_jobs) != 0:
		for job in pending_jobs:
			api_query = 'api/json/consoleText'
			uri = job + api_query
			result = requests.get(uri, auth=(user, pwd), verify=False)
			building = result.json()['building']
			if building is not True:
				status = result.json()['result']
				if status != 'SUCCESS':
					print "Job %s : %s" % (job, status)
					pending_jobs.remove(job)
					
				else:
					print "Job %s : %s" % (job, status)
					pending_jobs.remove(job)
					

	with open('backlog.py', 'w') as f:
		f.write('backlog = %s' % pending_jobs)

else:
	
	if len(pending_jobs) != 0:
		for job in pending_jobs:
			api_query = 'api/json/consoleText'
			uri = job + api_query
			result = requests.get(uri, auth=(user, pwd), verify=False)
			building = result.json()['building']
			if building is not True:
				status = result.json()['result']
				if status != 'SUCCESS':
					print "Job %s : %s" % (job, status)
					pending_jobs.remove(job)
				else:
					print "Job %s : %s" % (job, status)
					pending_jobs.remove(job)

	for x in running_jobs:
		if x not in pending_jobs:
			pending_jobs.append(x)



	with open('backlog.py', 'w') as f:
		f.write('backlog = %s' % pending_jobs)



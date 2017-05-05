import requests
from JenkinsApi import get_services

def get_criticality():
	
	#uri = "http://chexjvaord064:8500/v1/kv/?keys=true"
	#response = requests.get(uri)
	
	#services = set()
	#for keys in response.json():
	#	key = keys.split('/')[0]
	#	services.add(key)
	services = get_services()
	
	p1 = 0
	p2 = 0
	p3 = 0
	p1_services = []
	p2_services = []
	p3_services = []
	no_criticality = []
	
	for srv in services:
		url = "http://chexjvaord064:8500/v1/kv/%s/BASE/CRITICALITY?raw" % srv
		result = requests.get(url)
		criticality = result.text
		if criticality == 'P1':
			p1 += 1
			p1_services.append(srv)
		elif criticality == 'P2':
			p2 += 1
			p2_services.append(srv)
		elif criticality == 'P3':
			p3 += 1
			p3_services.append(srv)
		else:
			no_criticality.append(srv)
			
	return {'p1': p1, 
			'p2': p2, 
			'p3': p3, 
			'p1_services': p1_services, 
			'p2_services': p2_services, 
			'p3_services': p3_services,
			'services': services,
			'no_criticality': no_criticality
			}

def CalculatePercent():
	
	total_patched = 0
	p1_patched = 0
	p2_patched = 0
	p3_patched = 0
	no_criticality_patched = 0
	dummy_entries = []
	
	data = get_criticality()
	tot_serv = len(data['services'])
	no_criticality = len(data['no_criticality'])
	
	for srv1 in data['p1_services']:
		
		uri = 'http://chexjvaord064:8500/v1/kv/%s/PROD/PATCHING/?keys' % srv1
		keys = requests.get(uri)
		if keys.status_code == 200:
			key = keys.json()[0]
			url = 'http://chexjvaord064:8500/v1/kv/%s?raw' % key
			patch_verify = requests.get(url)
			out = patch_verify.text
			if 'CHG0320706' in out:
				total_patched += 1
				p1_patched += 1
		else:
			#tot_serv -= 1
			dummy_entries.append(srv1)
		
	for srv2 in data['p2_services']:
		
		uri = 'http://chexjvaord064:8500/v1/kv/%s/PROD/PATCHING/?keys' % srv2
		keys = requests.get(uri)
		if keys.status_code == 200:
			key = keys.json()[0]
			url = 'http://chexjvaord064:8500/v1/kv/%s?raw' % key
			patch_verify = requests.get(url)
			out = patch_verify.text
			if 'CHG0320706' in out:
				total_patched += 1
				p2_patched += 1
		else:
			#tot_serv -= 1
			dummy_entries.append(srv2)
		
	for srv3 in data['p3_services']:
		
		uri = 'http://chexjvaord064:8500/v1/kv/%s/PROD/PATCHING/?keys' % srv3
		keys = requests.get(uri)
		if keys.status_code == 200:
			key = keys.json()[0]
			url = 'http://chexjvaord064:8500/v1/kv/%s?raw' % key
			patch_verify = requests.get(url)
			out = patch_verify.text
			if 'CHG0320706' in out:
				total_patched += 1
				p3_patched += 1
		else:
			#tot_serv -= 1
			dummy_entries.append(srv3)
			
	for srv4 in data['no_criticality']:
		uri = 'http://chexjvaord064:8500/v1/kv/%s/PROD/PATCHING/?keys' % srv4
		keys = requests.get(uri)
		if keys.status_code == 200:
			key = keys.json()[0]
			url = 'http://chexjvaord064:8500/v1/kv/%s?raw' % key
			patch_verify = requests.get(url)
			out = patch_verify.text
			if 'CHG0320706' in out:
				total_patched += 1
				no_criticality_patched += 1
	
	actual_p1_services = len(data['p1_services'])
	actual_p2_services = len(data['p2_services'])
	actual_p3_services = len(data['p3_services'])
	
	#for entry in dummy_entries:
	#	if entry in actual_p1_services:
	#		actual_p1_services.remove(entry)
	#	elif entry in actual_p2_services:
	#		actual_p2_services.remove(entry)
	#	else:
	#		if entry in actual_p3_services:
	#			actual_p3_services.remove(entry)		
	
	p1_percent = int(float(p1_patched) /  len(data['p1_services']) * 100)
	p2_percent = int(float(p2_patched) /  len(data['p2_services']) * 100)
	p3_percent = int(float(p3_patched) /  len(data['p3_services']) * 100)
	#total_services = actual_p1_services + len(actual_p2_services) + len(actual_p3_services)
	total_percent = int(float(total_patched) / tot_serv * 100)
	#failed_services = tot_serv - ( p1_patched + p2_patched + p3_patched )
	no_criticality_percent = int(float(no_criticality_patched) / no_criticality * 100)
	
	return {'total_patched': total_patched,
			'p1_patched': p1_patched,
			'p2_patched': p2_patched,
			'p3_patched': p3_patched,
			'p1_percent': p1_percent,
			'p2_percent': p2_percent,
			'p3_percent': p3_percent,
			'tot_percent': total_percent,
			'tot_serv': tot_serv,
			#'total_services': total_services,
			#'dummy_entries': dummy_entries,
			'actual_p1_services': actual_p1_services,
			'actual_p2_services': actual_p2_services,
			'actual_p3_services': actual_p3_services,
			#'failed_services': failed_services
			'no_criticality' : no_criticality,
			'no_criticality_percent': no_criticality_percent,
			'no_criticality_patched': no_criticality_patched
			}
	
	
	
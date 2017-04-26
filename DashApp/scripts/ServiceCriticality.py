import requests

def get_criticality():
	
	uri = "http://chexjvaord064:8500/v1/kv/?keys=true"
	response = requests.get(uri)
	
	services = set()
	for keys in response.json():
		key = keys.split('/')[0]
		services.add(key)
	
	p1 = 0
	p2 = 0
	p3 = 0
	p1_services = []
	p2_services = []
	p3_services = []
	
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
			
	return {'p1': p1, 
			'p2': p2, 
			'p3': p3, 
			'p1_services': p1_services, 
			'p2_services': p2_services, 
			'p3_services': p3_services
			}

	
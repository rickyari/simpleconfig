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

def CalculatePercent():
	
	total_patched = 0
	p1_patched = 0
	p2_patched = 0
	p3_patched = 0
	
	data = get_criticality()
	
	for srv1 in data['p1_services']:
		try:
			uri = 'http://chexjvaord064:8500/v1/kv/%s/PROD/PATCHING/?keys' % srv1
			keys = requests.get(uri)
			key = keys.json()[0]
			url = 'http://chexjvaord064:8500/v1/kv/%s?raw' % key
			patch_verify = requests.get(url)
			out = patch_verify.text
			if 'CHG0320706' in out:
				total_patched += 1
				p1_patched += 1
		except ValueError:
			pass
		
	for srv2 in data['p2_services']:
		try:
			uri = 'http://chexjvaord064:8500/v1/kv/%s/PROD/PATCHING/?keys' % srv2
			keys = requests.get(uri)
			key = keys.json()[0]
			url = 'http://chexjvaord064:8500/v1/kv/%s?raw' % key
			patch_verify = requests.get(url)
			out = patch_verify.text
			if 'CHG0320706' in out:
				total_patched += 1
				p2_patched += 1
		except ValueError:
			pass
		
	for srv3 in data['p3_services']:
		try:
			uri = 'http://chexjvaord064:8500/v1/kv/%s/PROD/PATCHING/?keys' % srv3
			keys = requests.get(uri)
			key = keys.json()[0]
			url = 'http://chexjvaord064:8500/v1/kv/%s?raw' % key
			patch_verify = requests.get(url)
			out = patch_verify.text
			if 'CHG0320706' in out:
				total_patched += 1
				p3_patched += 1
		except ValueError:
			pass
	
	p1_percent = int(float(p1_patched) /  len(data['p1_services']) * 100)
	p2_percent = int(float(p2_patched) /  len(data['p2_services']) * 100)
	p3_percent = int(float(p3_patched) /  len(data['p3_services']) * 100)
	
	return {'total_patched': total_patched,
			'p1_patched': p1_patched,
			'p2_patched': p2_patched,
			'p3_patched': p3_patched,
			'p1_percent': p1_percent,
			'p2_percent': p2_percent,
			'p3_percent': p3_percent,
			}
	
	
	
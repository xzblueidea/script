import shodan

def shodanSearch(keywords):

	SHODAN_API_KEY = "x"
	api = shodan.Shodan(SHODAN_API_KEY)

	iplist = []
	total = 0

	try:
		results = api.search(keywords)
		total = int(results['total'])
		for result in results['matches']: iplist.append({"ip":result['ip_str'],"country":result['location']['country_name']})
		return total,iplist

	except shodan.APIError, e:
		print 'Error: %s' % e


print shodanSearch('netgear country:"AU"')

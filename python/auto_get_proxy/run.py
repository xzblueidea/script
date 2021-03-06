import random
import requests



def LoadUserAgents(uafile=''):
    uas = []
    with open(uafile, 'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[1:-1-1])
    random.shuffle(uas)
    return uas

# load the user agents, in random order
#user_agents = LoadUserAgents(uafile="user_agents.txt")



def LoadProxy(proxyfile=''):
    proxylist = []
    with open(proxyfile,'rb') as proxyf:
        for i in  proxyf.readlines():
            if i:
                proxylist.append(i.strip().split(' ')[4][:-1])
                #print list(i.strip())
    return proxylist

#LoadProxy('proxies.txt')


proxy = {"http": "http://username:p3ssw0rd@10.10.1.10:3128"}
url = 'http://api.openweathermap.org/data/2.5/weather'
params = {}

# load user agents and set headers
uas = LoadUserAgents(uafile="user_agents.txt")
ua = random.choice(uas)  # select a random user agent

# make the request
#r = requests.get(url, proxies=proxy, params=params, headers=headers)

import time

def main():
    proxy_list = LoadProxy('proxies.txt')
    for  p  in proxy_list:
        url = ''
        proxy  =  {"http": "http://%s"  % str(p.strip()) }
        print "proxy:"
        print proxy

        headers = {
            # "Connection" : "close",  # another way to cover tracks
                    "User-Agent" : ua}
        time.sleep(random.randint(0, 30))

        try:
            r = requests.get(url, proxies=proxy, params=params, headers=headers, timeout=2)
            print r.text
        except :
            pass


if __name__ == "__main__":
    main()




import requests
 
ip = requests.get('https://api.ipify.org').text
 
print('Show Public IP Address : {}'.format(ip))
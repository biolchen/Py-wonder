import requests
import sys
from subprocess import call

user = sys.argv[1]

r = requests.get('https://api.github.com/users/{0}/gists'.format(user))

for i in r.json():
	call(['git', 'clone', i['git_pull_url']])

	description_file = './{0}/description.txt'.format(i['id'])
	with open(description_file, 'w') as f:
		f.write('{0}\n'.format(i['description']))

'''
Referece: 
leoloobeek/get_gists.py
https://gist.github.com/leoloobeek/3be8b835988e8d926a4387019370db8d
'''

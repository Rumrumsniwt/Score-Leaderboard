#!/usr/bin/python3

# Score Leaderboard
# Author: Murmurtwins

import requests, json, math
url='https://akatsuki.pw/api/v1/scoreleaderboard?mode=0&p='
page=1
pagestr=str(page)
url2='&l=500&rx=1'
fullurl=url+pagestr+url2
r=requests.get(fullurl)
result=json.loads(r.text)
inf=result['users']
print('The score leaderboard for pp rank in range',page*500-499,'~',page*500,'is shown below:')

item=0
while item<=49:
	username=inf[item]['username']
	ranked_score=inf[item]['chosen_mode']['ranked_score']
	print(item+1,':',username,'|',ranked_score)
	item+=1

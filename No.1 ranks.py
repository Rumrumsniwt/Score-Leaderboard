#!/usr/bin/python3

# No.1 ranks
# Author: Murmurtwins

import requests, json, math
url='http://akatsuki.pw/api/v1/users/scores/first?mode=0&p='
page=13
pagestr=str(page)
url2='&l=100&rx=1&id=4391'
fullurl=url+pagestr+url2
r=requests.get(fullurl)
result=json.loads(r.text)
scores=result['scores']

print('On page',pagestr,'of API, you are No.1 on the following maps:')

def uppervalue(pgnum):
	if pgnum==1:
		return 55
	else:
		return 49

upper=uppervalue(page)
item=0
count=1
max_combomap=0
max_comboyou=0
misscount=0
pp=0
acc=0
information=''
while item<upper:
	pp=scores[item]['pp']
	max_combomap=scores[item]['beatmap']['max_combo']
	max_comboyou=scores[item]['max_combo']
	information=scores[item]['beatmap']['song_name']
	acc=scores[item]['accuracy']
	print(item+1,':',information,'|',acc,'%',max_comboyou,'/',max_combomap,pp,'pp')
	item+=1

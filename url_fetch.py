#!/usr/bin/env python3
# acamerlo@infoblox.com - june17
import time
import requests
from pandas.io.json import json_normalize
import pandas as pd
import sys
import codecs
# initialise
pd.set_option('display.max_colwidth', -1)
print(sys.version + '\n')
doc = {}
# read wapi call from file ( use vi + set noeol to edit/create )
with open('rest_call_url.txt', 'r') as fr:
   rest = fr.read()
# fetch from TIDE
for i in range(0, 5):
    while True:
        try:
            rekest = requests.get(str(rest), auth=(
                "xxxxxxAPIKEYxxxxxxxxx", ''))
        except requests.exceptions.ConnectionError as e:
            print("connection error, retry")
            continue
        break
print("Fetch OK")
# dig into json then normalise into dataframe
dic = rekest.json()
doc = dic['threat']
doc = json_normalize(doc)
# sort and reindex
doc = doc.sort_values("detected", 0, False)
doc = doc.reset_index(drop=True)
print("Convert ok")
# generate the HTML output
dphtml = r'<!DOCTYPE html><html>'
dphtml += r'<link rel="stylesheet" type="text/css" href="css-table.css">' + '\n'
dphtml += r'<html><head><title>TIDE URL THREATS</title></head><body>' + '\n'
dphtml += r'<p>Last 24hours URL threats extract - batch execution : ' + time.ctime() + '</p>' + '\n'
dphtml += r'<a href="rest_call.txt" target="_blank">link to rest request used</a>'
dphtml += doc.to_html()
dphtml += r'</body></html>'
print("Html generation OK")
# write do file
f = codecs.open('index.html', encoding='utf-8', mode='w+')
f.write(dphtml)
f.close()
# pass
print("write OK" + '\n')

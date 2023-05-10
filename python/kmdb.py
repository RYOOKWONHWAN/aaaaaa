import os
import sys
import requests
import json
import csv
import codecs


fieldnames = ['id', 'name', 'original_name', 'gender',
              'profile_path', 'known_for_department', 'character']

url = "http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json2.jsp?collection=kmdb_new2&ServiceKey=0E2600AFPUQOEJ2558Z8"
print(url)
res = requests.get(url)
json_data = res.json()
print(json_data)

import openpyxl
import os
import sys
import requests
import json
import csv
import codecs
from openpyxl.utils.cell import column_index_from_string

fieldnames = ["movie_id", "keyword_id", "keyword_name"]
if not os.path.isfile('keyword_data.csv'):
    with open('keyword_data.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
# 엑셀 파일 열기 (read-only 모드)
workbook = openpyxl.load_workbook('movie_list.xlsx', read_only=True)

# 원하는 시트 선택
worksheet = workbook['영화리스트']

# 특정 열 선택 (예시로 B열을 선택)
column_letter = 'D'
column_data = []
for row in worksheet.iter_rows():
    column_data.append(row[column_index_from_string(column_letter)-1].value)

# column_data에는 선택한 열의 데이터가 리스트 형태로 저장됩니다.
print(len(column_data))
for i in range(1, len(column_data)):
    url = "https://api.themoviedb.org/3/movie/" + \
        str(column_data[i]) + \
        "/keywords?api_key=3fa3ffb0e633bd85cdc1fe95f442cf6e"
    res = requests.get(url)

    json_data = res.json()

    movie_id = json_data['id']

   # CSV 파일에 데이터를 추가합니다 ('append' 모드 사용).
    with open('keyword_data.csv', mode='a', newline='', encoding='utf-8-sig') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        for genre in json_data['keywords']:
            writer.writerow({'movie_id': movie_id, 'keyword_id': genre.get(
                'id'), 'keyword_name': genre.get('name')})

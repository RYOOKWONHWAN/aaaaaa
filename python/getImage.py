import os
import sys
import requests
import json
import csv
import codecs
import openpyxl
from openpyxl.utils.cell import column_index_from_string
# CSV 파일에 저장할 필드명 정의
fieldnames = ["movie_id", "title", "original_title", "release_date", "popularity", "tmdb_vote_sum", "tmdb_vote_cnt",
              "overview", "poster_path", "backdrop_path", "country", "runtime"]
if not os.path.isfile('movie_fi.csv'):
    with open('movie_fi.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

# 여기에서 반복문을 시작하세요.

workbook = openpyxl.load_workbook('.xlsx', read_only=True)

# 원하는 시트 선택
worksheet = workbook['Sheet1']

# 특정 열 선택 (예시로 B열을 선택)
column_letter = 'A'
column_data = []
for row in worksheet.iter_rows():
    column_data.append(row[column_index_from_string(column_letter)-1].value)

# column_data에는 선택한 열의 데이터가 리스트 형태로 저장됩니다.
print(len(column_data))
for i in range(1, len(column_data)):  # 예제를 위한 임의의 반복문입니다.
    # ... 기존 코드 (예: API 호출)
    url = "https://api.themoviedb.org/3/movie/" + \
        str(column_data[i]) + \
        "?api_key=3fa3ffb0e633bd85cdc1fe95f442cf6e&language=ko-KR"

    print(url)
    res = requests.get(url)
    json_data = res.json()
  # 결과 목록 추출
    print(json_data)

   # CSV 파일에 데이터를 추가합니다 ('append' 모드 사용).
    with open('movie_detail.csv', mode='a', newline='', encoding='utf-8-sig') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if res.status_code == 200:
            country = ''
            for pc in json_data['production_countries']:
                country = pc.get('name')
                break
            print(country)
            overview = str(json_data['overview']).replace(
                '\n', '').replace('\r', '').replace('\r\n', '')
            writer.writerow({
                'adult': json_data['adult'],
                'backdrop_path': json_data['backdrop_path'],
                'id': json_data['id'],
                'original_language': json_data['original_language'],
                'original_title': json_data['original_title'],
                'overview': overview,
                'popularity': json_data['popularity'],
                'poster_path': json_data['poster_path'],
                'production_countries': country,
                'release_date': json_data['release_date'],
                'runtime': json_data['runtime'],
                'title': json_data['title'],
                'vote_average': json_data['vote_average'],
                'vote_count': json_data['vote_count']
            })

    print("CSV 파일에 데이터가 추가되었습니다.")

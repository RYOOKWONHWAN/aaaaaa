
import os
import folium
import cx_Oracle


# Oracle 데이터베이스 연결
dsn_tns = cx_Oracle.makedsn('localhost', 1521, service_name='xe')

LOCATION = r"C:\k_digital\util\instantclient_12_1"
os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]
conn = cx_Oracle.connect(user='hr9', password='a1234', dsn=dsn_tns)

# 쿼리 실행 및 결과 가져오기
cur = conn.cursor()
cur.execute('SELECT latitude, longitude FROM main_host')
rows = cur.fetchall()

# 지도 생성
map_center = [37.5642135, 127.0016985]  # 서울 중심 위도, 경도
m = folium.Map(location=map_center, zoom_start=12)

# 체육시설 위치 마커 추가
for row in rows:
    lat, lon = row[0], row[1]
    folium.Marker([lat, lon]).add_to(m)

# 지도를 HTML 파일로 저장
m.save('map.html')

# 연결 종료
cur.close()
conn.close()

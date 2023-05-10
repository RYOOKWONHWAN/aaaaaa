import csv
import datetime

# csv 파일에서 timestamp 값을 datetime 형식으로 변환하는 함수


def unix_time_to_datetime(unix_time):
    return datetime.datetime.fromtimestamp(int(unix_time)).strftime('%Y-%m-%d %H:%M:%S')


# 입력 파일 경로
input_file = 'ratings_small7.csv'

# 출력 파일 경로
output_file = 'rating_small7_new.csv'

# csv 파일 읽기
with open(input_file, 'r') as f:
    reader = csv.reader(f)
    # csv header
    header = next(reader)
    # 새로운 header
    new_header = header[:3] + ['timestamp_date'] + header[4:]
    # csv 내용
    rows = []
    for row in reader:
        # timestamp 값을 datetime으로 변환
        row[3] = unix_time_to_datetime(row[3])
        rows.append(row[:3] + [row[3]] + row[4:])

# csv 파일 쓰기
with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    # header 쓰기
    writer.writerow(new_header)
    # 내용 쓰기
    for row in rows:
        writer.writerow(row)

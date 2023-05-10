import pandas as pd

# MOVIE.csv 파일을 읽어옴
movies = pd.read_csv('python/MOVIE.csv')

# popularity 컬럼의 값이 15 이상인 데이터만 추출하여 저장
movies_filtered = movies[movies['popularity'] > 15]

# 추출한 데이터를 새로운 CSV 파일로 저장
movies_filtered.to_csv('python/MOVIE_FILTERED.csv', index=False)

# 결과 출력
print("Successfully saved the filtered data to 'python/MOVIE_FILTERED.csv'!")

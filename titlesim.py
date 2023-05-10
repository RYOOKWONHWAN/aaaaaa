# 사용자들의 평가 데이터를 기반으로 추천
# 참고 https://tpwkcorqhd.tistory.com/37
##

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity  # 코사인 유사도 산출하는 모듈


def titlesimdef(given_id):

    movies = pd.read_csv('python/MOVIE.csv')
    ratings = pd.read_csv('python/ratings_small4.csv')

    print('############################################')
    print(movies.shape)  # (9978,15)    9978개의 데이터와 15개의 컬럼을 갖는 행렬로 나옴
    print(ratings.shape)  # (100004,4)

    ratings = ratings[['userId', 'movieId', 'rating']]

    ratings_matrix = ratings.pivot_table(
        'rating', index='userId', columns='movieId')

    ratings_matrix = ratings_matrix.fillna(0)
    # # movies DataFrame에서 movieId와 title 컬럼만 추출합니다.
    # movie_to_idx = {
    #     row['movie_id']: row['title'] for idx, row in movies[['movie_id', 'title']].iterrows()
    # }

    # # ratings_matrix의 컬럼을 title로 변경합니다.
    # ratings_matrix.columns = [movie_to_idx.get(
    #     movie_id) for movie_id in ratings_matrix.columns]

    print('############################################')
    print(ratings_matrix.head(5))

    # 영화간의 유사도 산출
    print('############################################')
    ratings_matrix_T = ratings_matrix.transpose()
    print(ratings_matrix_T.head)

    item_sim = cosine_similarity(ratings_matrix_T, ratings_matrix_T)
    item_sim_df = pd.DataFrame(
        data=item_sim, index=ratings_matrix.columns, columns=ratings_matrix.columns)
    # 두개의 값이 같아야함
    # 영화제목을 행, 열로 유사도 분석하는 것
    print(item_sim_df.shape)

    # 제목을 코사인분석해서 비슷한걸 가져오는 것
    return item_sim_df[given_id].sort_values(ascending=False)[:10].index.tolist()

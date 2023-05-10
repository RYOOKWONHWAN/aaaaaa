# 사용자가 본 영화들의 장르를 기반으로 추천하는 알고리즘
# 시간이 오래걸린다. 영화 3개정도에 16초에서 20초 소모
# 최대 5개 까지 하는게 맞다고 생각
# 함수로 정의

# 참고 주소
# https://velog.io/@wltn39/%EB%8C%80%EB%B6%80%EC%99%80-%EC%9C%A0%EC%82%AC%ED%95%9C-%EC%98%81%ED%99%94-10%EA%B0%9C-%EC%B6%94%EC%B2%9C-CBF-%EA%B8%B0%EB%B0%98

import pandas as pd
import numpy as np
import warnings

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

warnings.filterwarnings('ignore')


def get_recommendations(given_id):
    def find_sim_movie_ver1(df, sorted_ind, movie_id, top_n=10):    # 코사인 유사도 산출 함수
        # df 에서 title 컬럼값이 title_name 인 df를 추출
        title_movie = df[df['movie_id'] == movie_id]

        # index 를 ndarray로 추출하고, 유사도 순으로 10개의 index 추출
        title_index = title_movie.index.values
        similar_indexes = sorted_ind[title_index, :(top_n)]

        # 추출된 데이터를 1차원으로 변환하고 해당 인덱스의 df 추출
        similar_indexes = similar_indexes.reshape(-1)
        return df.iloc[similar_indexes]

    def weighted_vote_average(record):  # 가중평균 계산 함수
        v = record['tmdb_vote_cnt']
        R = record['tmdb_vote_sum']

        return ((v/(v+m))*R)+((m/(m+v))*C)

    movies_df = pd.read_csv('python/MOVIE.csv', encoding='utf-8')
    genre_df = pd.read_csv(
        'python/merged_genre.csv', encoding='utf-8')

    genre_df['genre_dict'] = genre_df[['genre_id', 'genre_name']].apply(
        lambda x: {'id': x[0], 'name': x[1]}, axis=1)
    genre_dict_df = genre_df[['genre_id', 'genre_dict']]
    # 장르들을 하나의 리스트로 묶는다.
    genre_dict = genre_dict_df.set_index('genre_id').to_dict()['genre_dict']

    genre_df['genre_dict'] = genre_df['genre_id'].apply(
        lambda x: genre_dict.get(x))
    genre_df = genre_df.groupby(
        'movie_id')['genre_dict'].apply(list).reset_index()

    # 장르 df 와 무비 df 를 movie_id 를 기준으로 합친다.
    merged_df = pd.merge(movies_df, genre_df, on='movie_id', how='left')

    merged_df['genre_dict'] = merged_df['genre_dict'].apply(
        lambda x: [y['name'] for y in x] if isinstance(x, list) else [])

    merged_df['genres_literal'] = merged_df['genre_dict'].apply(
        lambda x: (' ').join(x))
    # gerne_dict 는 리스트기 때문에 이것을 스트링 값으로 바꿔준다.

    # CountVectorizer 학습
    # vectorizer(벡터화) 데이터를 선, 곡선 등 기하학적 모양으로 변환하는 것을 의미한다

    # 단어장에 들어갈 최소빈도(min_df), ngram(n개의 연속적인 단어 나열)의 범위
    count_vect = CountVectorizer(min_df=0, ngram_range=(1, 2))

    # 장르별 인덱스 사전
    genre_mat = count_vect.fit_transform(merged_df['genres_literal'])

    # 범위를 좁힌 CountVectorizer 학습

    # min_df: 단어장에 들어갈 최소빈도, ngram_range: 1 <= n <= 2
    count_vect2 = CountVectorizer(min_df=1, ngram_range=(1, 1))
    genre_mat2 = count_vect2.fit_transform(merged_df['genres_literal'])

    genre_sim = cosine_similarity(genre_mat, genre_mat)

    genre_sim_sorted_ind = genre_sim.argsort(
    )[:, ::-1]  # [:,::-1] 2차원 배열의 역순정렬
    genre_sim_sorted_ind[::-1]

    title_movie = merged_df[merged_df['movie_id'] == given_id]

    # 갓파더의 인덱스를 변수로 저장하고,
    title_index = title_movie.index.values

    # 코사인 유사도가 비슷한 영화의 인덱스 10개 추출
    similar_indexes = genre_sim_sorted_ind[title_index, :10]
    similar_indexes = similar_indexes.reshape(-1)
    # 1차원 array로 변경
    merged_df.iloc[similar_indexes].head(1)

    C = merged_df['tmdb_vote_sum'].mean()
    m = merged_df['tmdb_vote_cnt'].quantile(0.6)
    # print('C:', round(C, 3), 'm:', round(m, 3))

    #####################################################################
    # 가중치 추가
    merged_df['weighted_vote'] = merged_df.apply(weighted_vote_average, axis=1)

    merged_df[['weighted_vote', 'title', 'tmdb_vote_sum', 'tmdb_vote_cnt',
               'genre_dict']].sort_values('weighted_vote', ascending=False)[:10]
    # print('가중치 반영한 merged_df========================================================')
    # print(merged_df[['weighted_vote', 'title', 'vote_average', 'vote_count',
    #                  'genre_dict']].sort_values('weighted_vote', ascending=False)[:10])

    #####################################################################
    similar_movies = find_sim_movie_ver1(
        merged_df, genre_sim_sorted_ind, given_id, 20)   # 입력할 영화
    similar_movies[['title', 'tmdb_vote_sum', 'genre_dict', 'tmdb_vote_cnt']
                   ].head(1)
    # print('similar========================================================')
    # print(similar_movies['title'])
    # print(similar_movies)
    # print(similar_movies['weighted_vote'])
    # print(list(similar_movies.sort_values(
    #     'weighted_vote', ascending=False)[:10]['title'])
    # )
    return similar_movies.sort_values(
        'weighted_vote', ascending=False)[:10]

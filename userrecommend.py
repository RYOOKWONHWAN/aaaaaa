import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity  # 코사인 유사도 산출하는 모듈
from sklearn.metrics import mean_squared_error

# 예측 평점 구하는 함수
# 특정사용자가 특정 아이템에 대해 줄 평점을 예측하는 함수
# 개인에 맞춘 영화 추천


def userrecommenddef(given_user):
    def predict_rating(rating_arr, item_sim_arr):
        ratings_pred = rating_arr.dot(
            item_sim_arr)/np.array([np.abs(item_sim_arr).sum(axis=1)])
        return ratings_pred

    # mse 예측평가

    def get_mse(pred, actual):
        pred = pred[actual.nonzero()].flatten()
        actual = actual[actual.nonzero()].flatten()
        return mean_squared_error(pred, actual)

    # 예측 평가

    def predict_rating_topsim(rating_arr, item_sim_arr, n=20):
        pred = np.zeros(rating_arr.shape)
        for col in range(rating_arr.shape[1]):
            top_n_items = [np.argsort(item_sim_arr[:, col])[:-n-1:-1]]
            for row in range(rating_arr.shape[0]):
                pred[row, col] = item_sim_arr[col, :][top_n_items].dot(
                    rating_arr[row, :][top_n_items].T)
                pred[row,
                     col] /= np.sum(np.abs(item_sim_arr[col, :][top_n_items]))
        return pred

    def get_unseen_movies(ratings_matrix, userId):
        user_rating = ratings_matrix.loc[userId, :]
        already_seen = user_rating[user_rating > 0].index.tolist()
        movies_list = ratings_matrix.columns.tolist()
        unseen_list = [
            movie for movie in movies_list if movie not in already_seen]
        return unseen_list

    def recomm_movie_by_user_id(pred_df, userId, unseen_list, top_n=10):
        recomm_movie_list = pred_df.loc[userId, unseen_list].sort_values(ascending=False)[
            :top_n]
        return recomm_movie_list
    # # 행렬 분해를 이용한 잠재 요인 협업 필터링 ??
    # 사용 안할 수 도 있음
    # def get_rmse(R, P, Q, non_zeros):
    #     error = 0
    #     full_pred_matrix = np.dot(P, Q.T)
    #     x_non_zero_ind = [non_zero[0] for non_zero in non_zeros]
    #     y_non_zero_ind = [non_zero[1] for non_zero in non_zeros]
    #     R_non_zero_ind = R[x_non_zero_ind, y_non_zero_ind]
    #     full_pred_matrix_non_zeros = full_pred_matrix[x_non_zero_ind,
    #                                                   y_non_zero_ind]
    #     mse = mean_squared_error(R_non_zero_ind, full_pred_matrix_non_zeros)
    #     rmse = np.sqrt(mse
    #                    )
    #     return rmse

    movies = pd.read_csv('python/MOVIE.csv')
    ratings = pd.read_csv('python/ratings_small3.csv')

    ratings = ratings[['userId', 'movieId', 'rating']]

    ratings_matrix = ratings.pivot_table(
        'rating', index='userId', columns='movieId')

    ratings_matrix = ratings_matrix.fillna(0)
    # movies DataFrame에서 movieId와 title 컬럼만 추출합니다.
    movie_to_idx = {
        row['movie_id']: row['title'] for idx, row in movies[['movie_id', 'title']].iterrows()
    }

    # ratings_matrix의 컬럼을 title로 변경합니다.
    ratings_matrix.columns = [movie_to_idx.get(
        movie_id) for movie_id in ratings_matrix.columns]

    # print('############################################')
    # print(ratings_matrix.head(5))

    # 영화간의 유사도 산출
    # print('############################################')
    ratings_matrix_T = ratings_matrix.transpose()
    # print(ratings_matrix_T.head)

    item_sim = cosine_similarity(ratings_matrix_T, ratings_matrix_T)
    item_sim_df = pd.DataFrame(
        data=item_sim, index=ratings_matrix.columns, columns=ratings_matrix.columns)
    # 두개의 값이 같아야함
    # 영화제목을 행, 열로 유사도 분석하는 것
    # print(item_sim_df.shape)

    # print('예측 평점############################################')
    ratings_pred = predict_rating_topsim(
        ratings_matrix.values, item_sim_df.values)
    ratings_pred_matrix = pd.DataFrame(
        data=ratings_pred, index=ratings_matrix.index, columns=ratings_matrix.columns)
    # print(ratings_pred_matrix.head(5))

    # print("아이템기반 최근접 이웃 ", get_mse(ratings_pred, ratings_matrix.values))
    # 유저아이디가 9인 사용자가 평점을 준 영화들을 평점이 높은 순서대로
    # 그사람이 본 영화의 평가를 바탕으로 다른 모든 사용자가 평가한 정보를 코사인 유사도로 분석을해서
    # 9번 유저가 안본영화중에 예측평가의 점수가 가장 높은 10개를 가져와서 출력한다.
    # user_rating_id = ratings_matrix.loc[9, :]
    # user_rating_id[user_rating_id > 0].sort_values(ascending=False)[:10]
    # print(user_rating_id[user_rating_id > 0].sort_values(ascending=False)[:10])
    unseen_list = get_unseen_movies(ratings_matrix, given_user)
    recomm_movies = recomm_movie_by_user_id(
        ratings_pred_matrix, given_user, unseen_list, top_n=10)
    recomm_movies = pd.DataFrame(
        data=recomm_movies.values, index=recomm_movies.index, columns=['pred_score'])
    recomm_movies_list = recomm_movies.index
    return recomm_movies_list


#

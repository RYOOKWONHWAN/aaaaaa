import pandas as pd

genre_df = pd.read_csv('python/data_2023-04-24/genres_data.csv')
movie_detail_df = pd.read_csv('movie_fi.csv')

for index, row in genre_df.iterrows():
    movie_id = row['movie_id']
    genre_id = row['genre_id']
    genre_header = 'genre_' + str(genre_id)
    if genre_header in movie_detail_df.columns:
        movie_detail_df.loc[movie_detail_df['id']
                            == movie_id, genre_header] = 1

movie_detail_df.to_csv('new_csv_file.csv', index=False)

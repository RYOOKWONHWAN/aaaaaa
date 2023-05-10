from tkinter import *
import recommend


def get_movies():
    movies = "슈퍼 마리오 브라더스,샤잠! 신들의 분노,앤트맨과 와스프: 퀀텀매니아,아바타: 물의 길,크리드 3"

    movie_list2 = []
    movie_list1 = movies.split(',')
    for movie in movie_list1:
        movie = movie.strip()
        movie_list2.append(movie)

    # recommendation algorithm
    print(movie_list2)
    result = recommend.main(movie_list2)

    return result


print(get_movies())

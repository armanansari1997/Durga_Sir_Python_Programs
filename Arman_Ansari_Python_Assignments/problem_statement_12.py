from Day02 import movie_db


def check_score_greater_than_5(movie):
    return [True if movie['imdb'] > 5 else False]
    # if movie['imdb'] > 5:
    #     return True
    # else:
    #     False


def list_of_movies(movies):
    # for movie in movies:
    #     if check_score_greater_than_5(movie):
    #         movie_list.append(movie)
    # return movie_list

    # Recommended way
    movie_list = []
    word = [movie for movie in movies if check_score_greater_than_5(movie)]
    movie_list.append(word)
    return movie_list


def fn3(movie, category):
    return True if movie['category'] == category else False


def avg_imdb_score(movies):
    total_score = 0
    total_no_of_movies = len(movies)
    for movie in movies:
        total_score += movie['imdb']
    return total_score / len(movies)


if __name__ == '__main__':
    movies = movie_db.movies
    print(check_score_greater_than_5(movies[1]))

    print(list_of_movies(movies))

    print(fn3(movies[7], 'Romance'))

    list1 = [movie['name'] for movie in movies if fn3(movie,'Romance')]
    print(list1)

    print(avg_imdb_score([movies[0], movies[2], movies[4]]))

class Movie:
    """This class developed by Arman for Demo"""

    def __init__(self, title, hero, heroine):
        self.title = title
        self.hero = hero
        self.heroine = heroine

    def info(self):
        print('Movie name : ', self.title)
        print('Hero name : ', self.hero)
        print('Heroine name : ', self.heroine)


list_of_movies = []
while True:
    title = input('Enter Movie title : ')
    hero = input('Enter hero name : ')
    heroine = input('Enter Heroine name : ')
    m = Movie(title, hero, heroine)
    list_of_movies.append(m)
    print('Movie Added Successfully')
    option = input('Do you want to add one more movie[Yes/No]')
    if option.lower() == 'no':
        break

print('All Movie information')
for movie in list_of_movies:
    movie.info()
    print('-----------------------------')



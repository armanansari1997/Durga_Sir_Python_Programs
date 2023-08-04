# Same as Demo3 but using different way
class SportsNews:
    def sports_info(self):
        print("Sports Information - 1")
        print("Sports Information - 2")


class MoviesNews:
    def movies_info(self):
        print('Movies Information - 1')
        print('Movies Information - 2')


class PoliticsNews:
    def politics_info(self):
        print('Politics Information - 1')
        print('Politics Information - 2')


class DurgaNews:
    def __init__(self):
        self.sportsnews = SportsNews()
        self.moviesnews = MoviesNews()
        self.politicsnews = PoliticsNews()

    def get_total_news(self):
        print('Welcome to Durga News')
        self.sportsnews.sports_info()
        self.moviesnews.movies_info()
        self.politicsnews.politics_info()


dnews = DurgaNews()
dnews.get_total_news()


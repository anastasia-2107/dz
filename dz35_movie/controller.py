from view import UserInterface
from model import MovieModel


class Controller:
    def __init__(self):
        self.movie_model = MovieModel()
        self.user_interface = UserInterface()

    def run(self):
        answer = None
        while answer != 'q':
            answer = self.user_interface.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == "1":
            movie = self.user_interface.add_user_movie()
            self.movie_model.add_movie(movie)
        elif answer == "2":
            movies = self.movie_model.get_all_movies()
            self.user_interface.show_all_movies(movies)
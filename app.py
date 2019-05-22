from user import User
from movie import Movie

import os

import json

def menu():
    name = input("Welcome to the Movie App! What is your name? ")
    filename = "{}.txt".format(name)
    if file_exists(filename):
        with open(filename, 'r') as f:
            json_data = json.load(f)
        user = User.from_json(json_data)
    else:
        user = User(name)

    user_input = input("Enter 'a' to add a movie, 's' to see the list of movies, 'w' to set a movie as watched," 
                       "'d' to delete a movie, 'l' to see the list of watched movies, 'f' to save, or 'q' to "
                       "quit")
    while user_input != 'q':
        if user_input == 'a':
            new_movie = input("Enter the title of the movie you would like to add: ")
            new_genre = input("Now enter the movie's genre: ")
            new_watched = input("Have you watched this movie already? y/n:  ")
            if new_watched == 'y':
                new_watched = True
            else:
                new_watched = False
            user.add_movie(new_movie, new_genre, new_watched)

        elif user_input == 's':
            for movie in user.movies:
                print("Name: {}, Genre: {}, Watched: {}".format(movie.name, movie.genre, movie.watched))

        elif user_input == 'w':
            movie_name = input("Enter the movie name to set as watched")
            user.set_watched(movie_name)

        elif user_input == 'd':
            movie_name = input("Enter the movie name to delete: ")
            user.delete_movie(movie_name)

        elif user_input == 'l':
            for movie in user.watched_movies():
                print("Name: {}, Genre: {}, Watched: {}".format(movie.name, movie.genre, movie.watched))

        elif user_input == 'f':
            with open(filename, 'w') as f:
                json.dump(user.json(), f)

        user_input = input("Enter 'a' to add a movie, 's' to see the list of movies, 'w' to set a movie as watched,"
                           "'d' to delete a movie, 'l' to see the list of watched movies, 'f' to save, or 'q' to "
                           "quit")


def file_exists(filename):
    return os.path.isfile(filename)

menu()
import os
import csv
from datamanager.movie import *

class file:
    #
    # file class handles file operations for different movie
    # lists. Watched movies are being stored in files. File
    # format is CSV.
    #

    db_base_path = os.path.abspath("./data/")

    def __init__(self, fname, path = ""):
        self.fname = fname
        if path != "":
            self.db_base_path = path
        self.f_path = os.path.join(self.db_base_path, self.fname)
        
    def is_exists(self):
        if os.access(self.f_path, os.R_OK):
            return True
        return False

    def add_movie(self, new_movie):
        if not os.path.exists(self.db_base_path):
            os.mkdir(self.db_base_path)
        
        movie_dict = new_movie.as_dict()
        try:
            with open(self.f_path, "a+", newline="") as csv_file:
                fwriter = csv.DictWriter(csv_file, movie_dict.keys())
                fwriter.writerow(movie_dict)
        except Exception as e:
            print(f"E: {self.f_path}:")
            print(f"E: {e}")
    
    def get_movies(self):
        movie_list = []
        try:
            with open(self.f_path, "r", newline="") as mfile:
                reader = csv.DictReader(mfile, movie.get_fieldnames())
                for row in reader:
                    movie_list.append(movie.from_dict(row))
        except Exception as e:
            print(f"E: {self.f_path}:")
            print(f"E: {e}")
        return movie_list
        
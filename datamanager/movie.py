class movie:
    #
    # Movie class holds necessary information about the 
    #
    def __init__(self, name, director, year:int, grd1:int = 0, grd2:int = 0):
        self.name = name
        self.director = director
        self.year = year
        self.grd1 = grd1
        self.grd2 = grd2

    def from_dict(data_dict):
        new_movie = movie(data_dict["name"],
                          data_dict["director"],
                          int(data_dict["year"]),
                          int(data_dict["grd1"]),
                          int(data_dict["grd2"])
                          )
        return new_movie

    def get_fieldnames():
        return ["name", "director", "year", "grd1", "grd2"]

    def get_avg_grade(self):
        return int((self.grd1 + self.grd2) / 2 )

    def print_info(self):
        print(f"{self.name} ({self.year}) :", )
        print(f"- {self.director}")
        print(f"Avg Grade: {self.get_avg_grade()}")
    
    def review(self, grd1 = 5, grd2 = 5):
        self.grd1 = grd1
        self.grd2 = grd2
    
    def as_dict(self):
        return {"name": self.name,
                "director": self.director,
                "year": self.year,
                "grd1": self.grd1,
                "grd2": self.grd2}
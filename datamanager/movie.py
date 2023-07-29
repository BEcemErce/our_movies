class movie:
    #
    # Movie class holds necessary information about the 
    #
    def __init__(self, name, director, year, grd1 = 0, grd2 = 0):
        self.name = name
        self.director = director
        self.year = year
        self.grd1 = grd1
        self.grd2 = grd2

    def get_avg_grade(self):
        return int((self.grd1 + self.grd2) / 2 )

    def print_info(self):
        print(f"{self.name} ({self.year}) :", )
        print(f"- {self.director}")
        print(f"Avg Grade: {self.get_avg_grade()}")
    
    def review(self, grd1 = 5, grd2 = 5):
        self.grd1 = grd1
        self.grd2 = grd2
    
    def get_info_as_dict(self):
        return {"name": self.name,
                "director": self.director,
                "year": self.year,
                "grd1": self.grd1,
                "grd2": self.grd2}
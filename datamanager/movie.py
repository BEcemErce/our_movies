import datetime as dt

class movie:
    #
    # Movie class holds necessary information about the 
    #
    def __init__(self, name, date:dt.date, summary, grd1:int = 0, grd2:int = 0):
        self.name = name
        self.date = date
        self.summary = summary
        self.grd1 = grd1
        self.grd2 = grd2

    def from_dict(data_dict):
        movie_date = data_dict["date"].split("/")
        new_movie = movie(data_dict["name"],
                          dt.date(movie_date[2], movie_date[1], movie_date[0]),
                          data_dict["summary"],
                          int(data_dict["grd1"]),
                          int(data_dict["grd2"])
                          )
        return new_movie

    def get_fieldnames():
        return ["name", "date", "summary", "grd1", "grd2"]

    def get_avg_grade(self):
        return int((self.grd1 + self.grd2) / 2 )

    def print_info(self):
        print(f"{self.name} ({self.year}) :", )
        print(f"- {self.date}")
        print(f"- {self.summary}")
        print(f"Avg Grade: {self.get_avg_grade()}")
    
    def review(self, grd1 = 5, grd2 = 5):
        self.grd1 = grd1
        self.grd2 = grd2
    
    def as_dict(self):
        return {"name": self.name,
                "date": self.date,
                "summary": self.summary,
                "grd1": self.grd1,
                "grd2": self.grd2}
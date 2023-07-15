import requests

url = "https://api.themoviedb.org/3/search/movie?query=titanic"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwM2M3ODMxMWM0NzliYmM3M2VjMjNjZGJjNjE0ZjJlNCIsInN1YiI6IjY0YjJhNTcwMGJiMDc2MDE0ZTRlOTA3MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.TZaoMOx0yxlUlF6F_ILtwcMX3gvODRrIz4Zy8CNa-Ac",
    "query": "Titanic"
}

response = requests.get(url, headers=headers)

print(response.text)

###TO DO LIST ###
# Get specific movie.
# Create movie class.
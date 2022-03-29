import requests


class theMovieDb:
    def __init__(self):
        self.api_url = 'https://api.themoviedb.org/3/'
        self.api_key = '<YOUR_API_KEY>'

    def getPopulars(self):
        response = requests.get(
            f'{self.api_url}movie/popular?api_key={self.api_key}&language=en-US&page=1')
        return response.json()

    def getSearch(self, keyword):
        response = requests.get(
            f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()


movidb = theMovieDb()

while True:
    choice = input(
        '1. Popular Movies\n2. Search Movies\n3. Exit\nEnter your choice: ')

    if choice == 1:
        movies = movidb.getPopulars()
        for movie in movies['results']:
            print(f'{movie["title"]} ({movie["release_date"]})')

    elif choice == 2:
        keyword = input('Enter keyword: ')
        movies = movidb.getSearch(keyword)
        for movie in movies['results']:
            print(f'{movie["name"]} ({movie["first_air_date"]})')

    elif choice == 3:
        break
    else:
        print('Invalid choice')

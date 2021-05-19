import requests


def imdb_search(title):    

    url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

    querystring = {"s": title,"page":"1","r":"json"}

    headers = {
        'x-rapidapi-key': "b5a6dc6914msh268617fe992e521p1e1e0cjsn6a2da41f88ba",
        'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

userinput = input("Search for a movie, television show, video game or any type of media \n")
imdb_search(userinput)
if __name__ == "__api__":

    app.run()

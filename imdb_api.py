import requests


def imdb_search(title):    
    # url for the imdb api
    url = "https://movie-database-imdb-alternative.p.rapidapi.com/"
    # query string that includes what is being searched for, title is the parameter
    querystring = {"s": title,"page":"1","r":"json"}

    headers = {
        'x-rapidapi-key': "b5a6dc6914msh268617fe992e521p1e1e0cjsn6a2da41f88ba",
        'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
        }
    # stores the "GET" response in the response variable
    response = requests.request("GET", url, headers=headers, params=querystring)
    # prints out the response in text to the console
    print(response.text)

userinput = input("Search for a movie, television show, video game or any type of media \n")
# above line requests user input
imdb_search(userinput)
# calls function, passes argument of user input
if __name__ == "__api__":

    app.run()

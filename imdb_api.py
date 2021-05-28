import requests
import webbrowser


def imdb_search(title):    
    # url for the imdb api
    url = "https://movie-database-imdb-alternative.p.rapidapi.com/"
    # query string that includes what is being searched for, title is in the parameters
    querystring = {"s": title,"page":"1","r":"json"}

    headers = {
        'x-rapidapi-key': "b5a6dc6914msh268617fe992e521p1e1e0cjsn6a2da41f88ba",
        'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
        }
    # stores the "GET" response in the response variable
    response = requests.request("GET", url, headers=headers, params=querystring)
    # converts resulting text to a string
    string = str(response.text)
    # replaces commas with a new line/enter
    noComma = string.replace(",","\n ")
    # replaces " with nothing
    noQC = noComma.replace("\"","")
    # opens a new html document, stores it in the variable f
    f = open("simHTML1.html", "w")
    # takes the variable f and the open write method to write this information on the webpage

    f.write("""<html>
    <body><h1>{}<h1></body></html>""".format(noQC)) # formats input string and puts in document
    f.close()           
    webbrowser.open_new_tab("simHTML1.html")
    # returns the results
    #print(noQC)

userinput = input("Search for a movie, television show, video game or any type of media \n")
# above line requests user input
imdb_search(userinput)
# calls function, passes argument of user input
if __name__ == "__api__":

    app.run()

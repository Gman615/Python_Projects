from flask import Flask, jsonify

nba_teams = [
    {
        "id": 1,
        "city": "New York",
        "mascot": "Knicks",
        "colors": "blue and orange"
    },
    {
        "id": 2,
        "city": "Boston",
        "mascot": "Celtics",
        "colors": "green and white"
    },
    {
        "id": 3,
        "city": "Brooklyn",
        "mascot": "Nets",
        "colors": "black and white"
    },
    {
        "id": 4,
        "city": "Philadelphia",
        "mascot": "76ers",
        "colors": "blue and red"
    },
    {
        "id": 5,
        "city": "Washington",
        "mascot": "Wizards",
        "colors": "navy blue and red"
    },
        {
        "id": 6,
        "city": "Cleveland",
        "mascot": "Cavaliers",
        "colors": "wine red and gold"
    },
    {
        "id": 7,
        "city": "Charlotte",
        "mascot": "Hornets",
        "colors": "purple and teal"
    },
    {
        "id": 8,
        "city": "Atlanta",
        "mascot": "Hawks",
        "colors": "red and yellow"
    },
    {
        "id": 9,
        "city": "Detroit",
        "mascot": "Pistons",
        "colors": "blue and red"
    },
    {
        "id": 10,
        "city": "Milwaukee",
        "mascot": "Bucks",
        "colors": "green and gold"
    },
    {
        "id": 11,
        "city": "Chicago",
        "mascot": "Bulls",
        "colors": "red and black"
    },
        {
        "id": 12,
        "city": "Orlando",
        "mascot": "Magic",
        "colors": "blue and black"
    },
    {
        "id": 13,
        "city": "Miami",
        "mascot": "Heat",
        "colors": "red and black"
    },
    {
        "id": 14,
        "city": "Indiana",
        "mascot": "Pacers",
        "colors": "navy blue and yellow"
    },
    {
        "id": 15,
        "city": "Toronto",
        "mascot": "Raptors",
        "colors": "purple and red"
    },
    {
        "id": 16,
        "city": "New Orleans",
        "mascot": "Pelicans",
        "colors": "navy blue, gold, and red"
    },
    {
        "id": 17,
        "city": "Memphis",
        "mascot": "Grizzlies",
        "colors": "navy blue and light blue"
    },
    {
        "id": 18,
        "city": "Oklahoma City",
        "mascot": "Thunder",
        "colors": "light blue and orange"
    },
    {
        "id": 19,
        "city": "Denver",
        "mascot": "Nuggets",
        "colors": "navy blue, yellow, and red"
    },
    {
        "id": 20,
        "city": "Minnesota",
        "mascot": "Timberwolves",
        "colors": "Navy blue and green"
    },
    {
        "id": 21,
        "city": "Utah",
        "mascot": "Jazz",
        "colors": "green, purple, and yellow"
    },
    {
        "id": 22,
        "city": "Phoenix",
        "mascot": "Suns",
        "colors": "purple and orange"
    },
    {
        "id": 23,
        "city": "Portland",
        "mascot": "Trail Blazers",
        "colors": "red and black"
    },
    {
        "id": 24,
        "city": "Houston",
        "mascot": "Rockets",
        "colors": "red and white"
    },
    {
        "id": 25,
        "city": "Dallas",
        "mascot": "Mavericks",
        "colors": "navy blue and blue"
    },
    {
        "id": 26,
        "city": "San Antonio",
        "mascot": "Spurs",
        "colors": "black and silver"
    },
    {
        "id": 27,
        "city": "Los Angeles",
        "mascot": "Clippers",
        "colors": "blue and red"
    },
    {
        "id": 28,
        "city": "Los Angeles",
        "mascot": "Lakers",
        "colors": "purple and yellow"
    },
    {
        "id": 29,
        "city": "Golden State",
        "mascot": "Warriors",
        "colors": "blue and yellow"
    },
    {
        "id": 30,
        "city": "Sacramento",
        "mascot": "Kings",
        "colors": "purple and black"
    },
]


app = Flask(__name__)


@app.route("/")

def index():
    return "Hello world!"

@app.route("/library/v1.0/nba_teams/<int:nba_id>", methods=["GET"])
# this function requires a paramenter from the URL
def get_nba_teams(nba_id):
    # create an empty dictionary
    result = {}

    # Loops through all the different teams to find the one with the id that was entered.
    for nba_team in nba_teams:
        # checks if the id is the same as the parameter
        if nba_team["id"] == nba_id:
            # sets the result to the book and makes it a JSON.
            result = jsonify({"nba_team": nba_team})
    
    return result

if __name__ == "__main__":

    app.run()

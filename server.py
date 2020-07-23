"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


#add triple quotes in return to multiline html
#add link as <a href="link">description</a>
#link is /hello for app route to head to next
@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Start Here</title>
      </head>
      <body>
        <a href="/hello">Take me to the start</a>
      </body>
    </html>
    """


#add radio
@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""
# added radio and compliment request line
    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <p>What's your name? <input type="text" name="person"></p>
          <p>What compliment do you prefer?</p>
          <input type="radio" name="compliment" value="Pretty">Pretty</input>
          <input type="radio" name="compliment" value="Handsome">Handsome</input>
          <input type="radio" name="compliment" value="Awesome">Awesome</input>
          <input type="radio" name="compliment" value="Cool">Cool</input>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


#sub variables in curly braces, remove .format
@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")

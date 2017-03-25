# Instructions

1. Fork this repo on GitHub.
1. Create a program that can interactively play the game of Tic-Tac-Toe against a human
   player.
   * The program should win or draw, but never lose.
   * The human player should make the first move.
   * The program should announce the result of the game before clearing the board for
     another round of play.
1. Commit early and often, with good messages.
1. Push your code back to GitHub and send us a pull request.

# Implementation Guidelines

Your implementation should meet the following requirements:

* The game logic should be executed server-side (you pick the language/framework but we
  use a mix Django and Flask in Python).
* The interface for the game should be a JavaScript Single Page App (SPA) running
  in a browser (again, you pick the frameworks/toolchains but we use a mix of React and
  Angular 1.x).
* You should rewrite this `README.md` to include build/run instructions for your apps
  (both client and server).

For a little extra credit:

* The SPA should _not_ be hosted by the server-side app, but instead through a separate
  server process (the client app should be completely standalone).


# Install Instructions for the Flask App

1. Clone the repo locally. `git clone git@github.com:smbsimon/web-code-test.git`
1. Install a virtual environment. (I like virtualenv.) `pip install virtualenv`
1. Change into the project directory. `cd web-code-test`
1. Create a virtual environment for the app. `virtualenv venv`
1. Enter the virtual environment. `source venv/bin/activate`
1. Install Flask. `pip install Flask`
1. Set Flask instance. `export FLASK_APP=game.py`
1. Run the app. `flask run`

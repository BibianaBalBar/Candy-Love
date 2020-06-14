# Candy Love
Python and Flask social media web app.    

Users can list their favorite candies, follow other users and see posts from friends and all users

![candyLove](https://github.com/BibianaBalBar/Candy-Love/blob/master/img/candy-love.png)

## Deployed at: 
http://candy-love-flask.herokuapp.com/

To test it create your own user or use:\
Username: Cindy\
Password: cindy

## To run in your local server:
Requirements: Python 3.6+, python-pip, virtualenv

Clone this repo:
        
        $ git clone https://github.com/BibianaBalBar/Candy-Love

        $ cd Candy-Love


Create Virtual enviroment:
        
        $ python3 - venv env

        $ source env/bin/activate

        (env) $ 

Install all requirements:
        
        $ pip install -r requirements.txt

Set flask environment: (for windows use set command)

        (env) $ export FLASK_APP=microblog.py

Run the app:

        (env) $ flask run

# Questions

Questions need answers. Preferably true ones. Or as close to the truth as possible. This is a webservice
to make that easier.

# Setup

Make a virtualenv for django:

    mkvirtualenv questions

then install all requirements:

    pip install -r requirements.txt

And run all migrations

    python manage.py migrate

# Config

See `questions/settings.py` for all settings. For local development, it should be enough to create a `.env` file containing
 the following settings:

    SECRET_KEY=<some random key>
    DEBUG=True
    DATABASE_URL=sqlite:////<path to project>/questions/db.sqlite3

# Testing

To run locally at http://127.0.0.1:8000/

    python manage.py runserver

To run tests:

    python manage.py runserver


# Sample data

Import the example data:

    python manage.py loaddata example.json

To play about with it, go to http://127.0.0.1:8000/
Use the following:

     user: admin
     password: adminPassword


# Deployment

The project is currently deployed on [Heroku](https://dashboard.heroku.com/apps/odpowiedzi). To deploy it, one must first have heroku
CLI [set up](https://devcenter.heroku.com/articles/getting-started-with-python#set-up). Next, commit any changes and push them to
heroku:

     git push -f heroku master

 To change any config settings, it should suffice to change the appropriate env variables (can be done via the
 [web console](https://dashboard.heroku.com/apps/odpowiedzi/settings)). To run any migrations, execute:

     heroku run python manage.py migrate

# Questions

Questions need answers. Preferably true ones. Or as close to the truth as possible. This is a webservice
to make that easier.

# Setup

## Backend

Make a virtualenv for django:

    mkvirtualenv questions

then install all requirements:

    pip install -r requirements.txt

And run all migrations

    cd questions
    python manage.py migrate

## Frontend

Make sure you have node.js installed

    sudo apt intstall npm


# Testing

To run locally at http://127.0.0.1:8000/

    python questions/manage.py runserver

To run tests:

    python questions/manage.py runserver


# Sample data

Import the example data:

    python questions/manage.py loaddata example.json

To play about with it, go to http://127.0.0.1:8000/
Use the following:

     user: admin
     password: adminPassword

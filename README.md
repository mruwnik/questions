# Questions

Questions need answers. Preferably true ones. Or as close to the truth as possible. This is a webservice
to make that easier.

# Setup

Make a virtualenv for django:

    mkvirtualenv questions

then install all requirements:

    pip install -r requirements.txt

And run all migrations

    python questions/manage.py migrate


# Testing

To run locally at http://127.0.0.1:8000/

    python questions/manage.py runserver

To run tests:

    python questions/manage.py runserver

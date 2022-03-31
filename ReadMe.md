Ambient Weather Server
======================

This is a simple Flask Python app that will listen for input from an Ambient Weather weather station, storing the data into a MySQL/MariaDB table.

Right now it just stores the data exactly as given. What you do with the data is up to you!

###To set it up

Clone this repo to your server. Assuming you have Python and pip installed:

    pip install virtualenvwrapper
    mkvirtualenv aw-server
    workon aw-server
    pip install Flask flask-mysql gunicorn

You will need to get the MAC address for your station from the setup app.

Create a MySQL or MariaDB database, and create the weather table in it by running the SQL in table.sql.

Edit the config.json file with the DB connection information, and the MAC address in PASSKEY (the Ambient Weather API passes this as PASSKEY to authenticate itself).

For testing purposes, you can run the app like this (where SERVER_IP is the IP address of your server):

    gunicorn -bind SERVER_IP:5000 wsgi:app

If you want to run the app in the background, add the --daemon option:

    gunicorn --daemon -bind SERVER_IP:5000 wsgi:app

Once the server is running, in the setup app, go to the Customized screen, and fill in your server IP, a path of `/?` a port of 5000 (or whatever port you used in the gunicorn command), and change the interval to your preference, then hit Save.

The DB should start getting entries now.

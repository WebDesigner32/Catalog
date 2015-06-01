##**Landon's Restaurant Menu App**##

##**Project Goals**##

This project aims to make use of the Flask framework where restaurants are
listed with their menus. Using third-party authentication by way of Google+
or fb, logged-in users can: create, update, and delete their own restaurants
and corresponding menus.

##**Configuration Instructions**##

This project requires:

1. Python Libraries: requests, oauth2client, and httplib2
2. Python 2.7
3. SQLite
4. SQLAlchemy
5. Flask 0.10.1

##**Installation Instructions**##

Assuming you have downloaded the application code, navigate to the directory
where database_setup.py lives and run: `python database_setup.py`.* This will
set up the database. Once the database is created you can run
`python lotsofmenus.py` (assuming lotsofmenus.py is in the same directory
database_setup.py lives), to populate the database with useful prearranged
content.

* I use Vagrant, so in your case you want to start by specifying the path you
stored this project in on the command line. Then run `vagrant up` followed by
`vagrant ssh`, if you use Vagrant and it is set up in the location of the
project on your computer. If you do not use Vagrant, then install SQLAlchemy
from the following link: http://www.sqlalchemy.org.

##**Operating Instructions**##

Here we have a list of API endpoints used in this project:

1. https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s
2. https://graph.facebook.com/v2.3/me
3. https://graph.facebook.com/v2.3/me?%s
4. https://graph.facebook.com/v2.3/me/picture?%s&redirect=0&height=200&width=200
5. https://graph.facebook.com/%s/permissions/%s
6. https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s
7. https://www.googleapis.com/oauth2/v1/userinfo
8. https://accounts.google.com/o/oauth2/revoke?token=%s

##**How to Run Code**##

1. Run `python project.py` in the appropriate path.*
2. Go to your web browser and input: `http://localhost:5000`.
3. In the top-right of the page for the app, click "Click Here to Log in".
4. Ignoring Google+ due to my personal login information, log in with fb using
the following test user info to use the app:

Email: developer32@hotmail.com, Password: 5H@!u?k9s#

* I use Vagrant, so in your case you want to specify the path you stored this
project in on the command line. Then run `vagrant up` followed by
`vagrant ssh`, if you use Vagrant and it is set up in the location of the
project on your computer. If you do not use Vagrant, then install SQLAlchemy
from the following link: http://www.sqlalchemy.org.

##**Sources**##

1. The opensource banner maker that I used to create my banner can be found at:
`http://bannerfans.com/banner_maker.php`.

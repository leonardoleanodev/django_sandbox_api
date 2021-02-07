
# How to run the microservice:

`cd django_sando_box_api`
`python manage.py migrate`
`python manage.py runserver`


# For profuction:

- remove the secret key from settings and use environment variables to it not be availabel via repository, use something to encript the settings to load befor the runserver

- reconfigure the database to a more secure one, in this project we are using sqlile, it would be bether to use a postgres or other relacional database

-

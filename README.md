# How to setup the project

`python -m virtualenv venv`
`source venv/bin/activate`
`pip install -r requirements.txt`

# How to run the microservice:

`cd django_sando_box_api`
`python manage.py migrate`
`python manage.py runserver`

# creating a new user for the application

`python manage.py createsuperuser`

# For profuction:

- remove the secret key from settings and use environment variables to it not be availabel via repository, use something to encript the settings to load befor the runserver

- reconfigure the database to a more secure one, in this project we are using sqlile, it would be bether to use a postgres or other relacional database

-

# testing the api in a python terminal

```
>>> import requests
>>> requests.get('http://localhost:8000/aec/api/v1/')
>>> res = requests.post('http://localhost:8000/aec/api/v1/signin', data={'username':'admin','password':'admin'})
>>> token = res.json()['token']
>>> requests.get('http://localhost:8000/aec/api/v1/user_info', headers={'Authorization': f'Token {token}'})
```
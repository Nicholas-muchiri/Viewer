# [Viewer](https://nicholasgallary.herokuapp.com/)
### A web application used to post images according to location and category.

#### By **[Nicholas Muchiri](https://github.com/Nicholas-muchiri)**

## Description
[Viewer]((https://nicholasgallary.herokuapp.com/)) is a simple A web application used to post images according to location and category.. Users get to view photos updated by the site admin.  They can also copy the link to a photo to paste at their discretion. The search functionality will search photos based on the categories. 

## Set Up and Installations

### Prerequisites
1. Ubuntu Software
2. Python3.6
3. [Postgres](https://www.postgresql.org/download/)
4. [python virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)

### Clone the Repo
Run the following command on the terminal:
`git clone https://github.com/Nicholas-muchiri/Viewer.git && cd Viewer`

### Activate virtual environment
Activate virtual environment using python3.6 as default handler
```bash
virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate
```

### Install dependancies
Install dependancies that will create an environment for the app to run
`pip3 install -r requirements.txt`

### Create the Database
```bash
psql
CREATE DATABASE gallery;
```
### .env file
Create .env file and paste paste the following filling where appropriate:
```python
SECRET_KEY = '<Secret_key>'
DBNAME = 'gallery'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True
```
### Run initial Migration
```bash
python3.6 manage.py makemigrations pictures
python3.6 manage.py migrate
```

### Run the app
```bash
python3.6 manage.py runserver
```
Open terminal on `localhost:8000`

## Known bugs
no bugs. 

## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - JavaScript
    - Heroku
    - Postgresql

## Support and contact details
Contact me on Nickromero@gmail.com for any comments, reviews or advice.

### License
Copyright (c) **Nicholas Muchiri**
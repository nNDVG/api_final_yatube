# Discription
## Project "API for Yatube"
#### The API for Yatube project is part of a larger project to create a social networking site for Yatube personal blogs.The task of the project is to create an API for organizing access to the "Yatube" social network. Data transfer is carried out using the HTTP protocol. REST API principles apply. The server responds in JSON format. Authentication is performed using a JWT token. 
#### API address: http: // localhost: 8000 / api / v1 /
#### Documentation with example commands: http: // localhost: 8000 / redoc /
### What would add:
- With the addition of private messages in the main project, delete and manage them via API

## Using the API, you can access the following models:
    POSTS - Author publications (view, create, edit, delete)
    COMMENTS - Comments on authors' publications (view, create, edit, delete)
    FOLLOW - Subscription to authors of publications (view, create)
    GROUP - Groups of authors of publications (viewing, creating)
    AUTH - Get JWT token (get, refresh)

# RUN
### To install on a local machine, you will need:

    Download project files from the repository
    Install dependencies from requirements.txt file
    Run the server with the python manage.py runserver command from the project root

# TESTS
#### Run the command in the project directory (with file the "pitest.ini" file):

    pytest

# Author
- https://github.com/nNDVG/
- https://hub.docker.com/u/ndvg/
### Contacts
- Telegram: nNDVG
- Email: n.dvg@yandex.ru

# Tech stack:
- Python3.x
- Django
- Django REST



# Doctor_online

## Desc: The task is to build api CRUD'S for users(doctor or patient) can register, login and resreve a clinic
## ER Diagram For DB
![DatabaseDiagram](https://user-images.githubusercontent.com/19196061/115124959-87c2db00-9fc5-11eb-8e54-f423eef6d320.jpeg)
## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/MohamedAhmed7/Doctor_online.git
$ cd Doctor_online
```
Create a virtual environment to install dependencies in and activate it:

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd Doctor_online
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```
API Main Endpoints
```sh
http://localhost:8000/users/
http://localhost:8000/clinics/
http://localhost:8000/reservations/
```




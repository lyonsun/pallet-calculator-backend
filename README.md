This is the backend part of the pallet calculator web application, it is built with `django` and `djangorestframework`.
Find the frontend part of it here: https://github.com/lyonsun/pallet-calculator-frontend

## Clone it

```shell
git clone git@github.com:lyonsun/pallet-calculator-backend.git
```

## Activate new dev env

```shell
python -m venv env
source env/bin/activate
```

## Update pip

```shell
pip install --upgrade pip
```

## Install all dependencies

```shell
pip install -r requirements.txt
pip freeze > requirements.txt
```

## Data migration

```shell
python manage.py makemigrations
python manage.py migrate
```

## Run it

```shell
python manage.py runserver
```

## View it

Open the browser and go to http://localhost:8000/api/
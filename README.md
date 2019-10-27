# djangoRestFremwork_template
# Create django virtual environment
pipenv install django

# Create Django project
django-admin startproject helloworld_proj .

# Run django server
python3 manage.py runserver

# create new module inside django project called main_app
python3 manage.py startapp main_app

# active env shell
source /home/munim/anaconda3/bin/activate
conda activate base
source /home/munim/.local/share/virtualenvs/product1-rJwyOw6d/bin/activate

# install psycopg2 for postgres database connection
pipenv install psycopg2

# for psycopg2 troubleshooting 
sudo apt install libpq-dev python3-dev
pipenv install psycopg2

# database migration 
python3 manage.py makemigration
python3 manage.py migrate

# Create super user for django admin plan
python3 manage.py createsuperuser

# install djangorestframework
pipenv install djangorestframework

# Create new app for djangoRestFramwork
python3 manage.py startapp api
python3 manage.py runserver

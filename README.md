# Django CRUD

in this lab we started working with django, here is the steps we followed to creat the project and its app:

1. create a poetry new project and give it the desired name
2. poetry install 
3. git init
4. poetry shell
5. poetry add django 
6. remove the porject and the test folders
7. use `django-admin startproject project_name`
8. use `python manage.py migrate` to set the database
9. use `python manage.py createsuperuser` to assign superuser
10. use `python manage.py runserver` to check everything is ok and the server works fine
11. inside the project folder use `python manage.py startapp app_name` to make a new app
12. inside the settings.py of the project add the app name to the installed_apps list
13. add models to the models.py in the app
14. create views -using templates- inside the views.py of the app
15. add urls.py in the app folder and add to it the desired paths
16. add the app urls.py to the projects urls.py , using include and import include in the top
17. add `BASE_DIR / 'templates'` to the settings.py under TEMPLATES-> "DIRS" list
18. after each adding to a model use `python manage.py makemigrations` and then `python manage.py migrate`
-----
## in this lab
in this lab we created the CRUD for the snacks, we created a view for list, detail, update , create and delete.

## pull request link 
https://github.com/SalimHass/django-models/pull/1


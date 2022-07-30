To run project from docker follow instruction:
1. Run " docker-compose run web django-admin startproject inforce-task " from project dir
2. Run " docker-compose up "
3. " docker ps "
4. " docker exec -t -i CONTAINER ID bash "
5. " manage.py makemigrations "
6. " manage.py migrate "
7. " manage.py createsuperuser "
8. " flake8 " to run flake8
9. " pytest " to run pytest

If project expediently start before database run " python manage.py runserver 0.0.0.0:8000 " into docker shell
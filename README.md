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

Task info:

INFORCE PYTHON TASK

Try to write effective and understandable code for any programmer, and
document the code (without fanaticism, in places with complex logic, you can
write comments, but if you support SOLID principles, everything will be clear
in principle anyway). Take into account, that on almost all projects you have
to work in a team, and you have to make them feel comfortable working with
you.

Think about what you write, take the logic to separate modules/services,
write so that you don't have to sit and disassemble the function for 500
lines, and disassemble the logic into small tasks, this increases readability
and reusability. The main thing is not just to do it or to do it quickly, but to do
it qualitatively, to show what you can do.

ACTUAL TASK:

A company needs internal service for its 'employees which helps them to
make a decision at the lunch place. Each restaurant will be uploading menus
using the system every day over API.

Employees will vote for the menu before leaving for lunch on a mobile app
for whom the backend has to be implemented. There are users who did not
update the app to the latest version and the backend has to support both
versions. The mobile app always sends the build version in headers

API FUNCTIONALITY:
- Authentication
- Creating restaurant
- Uploading menu for restaurant (There should be a menu for each day)
- Creating employee
- Getting current day menu
- Getting results for the current day

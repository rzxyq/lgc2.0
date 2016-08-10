Instructions:

Use virtualenv if you have one. If not, you can also install this directly.

1. Make sure you have python 3 instead of python 2. Then do "pip install -r requirements.txt" in the root directory (lgc).

2. This app uses postgresql as database. Download postgresql then run "postmaster" or equivalent "brew services start postgresql" in a new terminal window.
If it's your first time using postgres, do "brew info postgres", "export PGDATA=/usr/local/var/postgres" if configuration for server not found.
Then "createdb $(YOUR USER NAME)" and "psql" to view tables from comman line.
Useful commands:
\dt
\q
When running into a psycopg image not found error, do "export DYLD_FALLBACK_LIBRARY_PATH=$HOME/anaconda/lib/:$DYLD_FALLBACK_LIBRARY_PATH"

If you want to use the admin interface, "python manage.py createsuperuser"

3. Make sure postgresql's running correctly, then do "python manage.py makemigrations" and "python manage.py migrate".

4. "python manage.py collectstatic"

5. To test on local server, run "python manage.py runserver". Open browser and go to "localhost:8000" and you'll see the website.


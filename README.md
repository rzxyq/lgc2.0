Instructions:

Use virtualenv if you have one. If not, you can also install this directly.

1. Make sure you have python 3 instead of python 2. Then do "pip install requirements.txt" in the root directory (lgc).

2. This app uses postgresql as database. Download postgresql then run "postmaster" in a new terminal window.

3. Make sure postgresql's running correctly, then do "python manage.py makemigrations" and "python manage.py migrate".

4. "python manage.py collectstatic"

5. To test on local server, run "python manage.py runserver". Open browser and go to "localhost:8000" and you'll see the website.


https://docs.djangoproject.com/en/3.1/intro/tutorial02/

## Setup

- Create a new virtual env: `$ python3 -m venv ctenv`
- Activate the env: `$ source ctenv/bin/activate`
- After activation you will see that the prompt in your console is prefixed with (ctenv)
- Upgrade pip: `(ctenv) ~$ python -m pip install --upgrade pip`
- Create [requirements.txt](#requirements) in your project root directory with `Django~=3.2`
- Install Django: `pip install -r requirements.txt`
- Run the application: `(ctenv) ~$ python manage.py runserver`
- See the app on: http://127.0.0.1:8000
- See the admin interface on: http://127.0.0.1:8000/admin

- Stop the server by ctrl-c
- Quit venv by `deactivate` or ctrl-d

### Secret key

Django genrates a secret key which should not be deployed to public repos. It is a good practice to store the key as env variable.

In your bashrc/zshrc file:
SECRET_DJANGO_KEY='yourkey'

In settings.py;
import os
SECRET_KEY = os.environ['SECRET_DJANGO_KEY']

SECRET_KEY = 'SECRET_KEY'

--


## The app

- Setup pyenv & Django
- SqlLite of Postgress (sql3 is leaner for testing)
- Setup poll app
- Setup database provisioning

## Branch: Case unit tests

Run the app and vote. Everything seems cool.
Run the unit tests
The poll count is not working/off by one
Fix
Running fine

## Branch: Case E2e tests

Run the app and vote. Everything seems cool.
Click on detail/result link error
Run e2e tests: error
Fix

## Branch Integration test



##requirements

###### Requirements without Version Specifiers
nose
nose-cov
beautifulsoup4

###### Requirements with Version Specifiers
docopt == 0.6.1             # Version Matching. Must be version 0.6.1
keyring >= 4.1.1            # Minimum version 4.1.1
coverage != 3.5             # Version Exclusion. Anything except version 3.5
Mopidy-Dirble ~= 1.1        # Compatible release. Same as >= 1.1, == 1.*

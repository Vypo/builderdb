# BuilderDB

BuilderDB is a website for reviewing costume builders.

## Setup

    $ virtualenv venv  
    $ . ./venv/bin/activate  
    $ pip install -r requirements.txt  
    $ ./manage.py migrate  
    $ ./manage.py sitetree_resync_apps  
    $ ./manage.py runserver

For more information, see https://www.djangoproject.com/

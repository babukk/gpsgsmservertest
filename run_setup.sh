#! /bin/sh
#--------------------------------------------------------------------------------------------------------------------------------------------

SERVER_DIR="."
cd ${SERVER_DIR}

if [ ! -d .venv3 ]; then
    virtualenv -p `which python3` ${SERVER_DIR}/.venv3/
    . ${SERVER_DIR}/.venv3/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    pip freeze
else
    . ${SERVER_DIR}/.venv3/bin/activate
fi

if [ ! -d gpsserver ]; then
    django-admin startproject gpsserver .
    sed -i '$s/$/\nSTATIC_ROOT = os.path.join(BASE_DIR, "static")\n/' gpsserver/settings.py
    sed -i '$s/$/\ntry:\n    from .local_settings import *\nexcept ImportError:\n    pass\n/' gpsserver/settings.py
fi

if [ ! -d gpsserver/static ]; then
    mkdir -p gpsserver/static
    python manage.py collectstatic
fi

if [ ! -d users ]; then
    python manage.py startapp users
fi

# python manage.py test

# python manage.py makemigrations --dry-run --verbosity 3
# python manage.py makemigrations gpsserver
#python manage.py makemigrations
#python manage.py migrate

# python manage.py createsuperuser

python manage.py runserver 0.0.0.0:8888

deactivate


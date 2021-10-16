#!/bin/sh

sleep 5

if test ! -f /opt/dani_shop/.first.txt;
then
    rm -rf /opt/dani_shop/dani_shop/migrations
    python3 /opt/dani_shop/dani_shop/manage.py collectstatic --no-input
    python3 /opt/dani_shop/dani_shop/manage.py flush --no-input

    touch /opt/dani_shop/.first.txt;
else
    /usr/bin/pip3 install -r /opt/dani_shop/requirements.txt
    python3 /opt/dani_shop/dani_shop/manage.py collectstatic --no-input
fi

python3 /opt/dani_shop/dani_shop/manage.py makemigrations register_bot
python3 /opt/dani_shop/dani_shop/manage.py migrate register_bot
python3 /opt/dani_shop/dani_shop/manage.py makemigrations assistance_bot
python3 /opt/dani_shop/dani_shop/manage.py migrate assistance_bot

python3 /opt/dani_shop/dani_shop/manage.py loaddata /opt/dani_shop/dani_shop/dani_shop/fixtures/users.json
python3 /opt/dani_shop/dani_shop/manage.py loaddata /opt/dani_shop/dani_shop/dani_shop/fixtures/applications.json
python3 /opt/dani_shop/dani_shop/manage.py loaddata /opt/dani_shop/dani_shop/dani_shop/fixtures/accesstokens.json
python3 /opt/dani_shop/dani_shop/manage.py loaddata /opt/dani_shop/dani_shop/assistance_bot/fixtures/channels.json
python3 /opt/dani_shop/dani_shop/manage.py loaddata /opt/dani_shop/dani_shop/assistance_bot/fixtures/topics.json

exec "$@"

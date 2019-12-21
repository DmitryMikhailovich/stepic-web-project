DIR=$(dirname "$0")
mkdir /etc/gunicorn.d
cp -r -f $DIR/web /home/box
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/ask.py /etc/gunicorn.d/ask.py

source $DIR/create_db.sh
python $DIR/web/ask/manage.py makemigrations
python $DIR/web/ask/manage.py migrate

gunicorn --config=/etc/gunicorn.d/hello.py hello:application &
gunicorn --config=/etc/gunicorn.d/ask.py ask.wsgi:application &
sudo nginx -s reload
wait



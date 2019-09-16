cp -r -f ./web /home/box
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py

gunicorn --config=/etc/gunicorn.d/hello.py hello:application

sudo nginx -s reload



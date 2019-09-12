cp -r -f ./web /home/box
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo nginx -s reload

sudo ln -s /home/$(whoami)/web/etc/nginx.conf /etc/nginx/conf.d/stepic.conf
sudo nginx -s reload

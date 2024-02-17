ssh tanishq@64.227.160.102 
pass - MyPass@12345

sudo apt update
# ---------------------------------------------------
sudo apt install python3-pip python3-dev nginx
# ---------------------------------------------------
sudo pip3 install virtualenv
# ---------------------------------------------------
mkdir ~/restrauntify
# ---------------------------------------------------
cd ~/restrauntify
# ---------------------------------------------------
virtualenv env
# ---------------------------------------------------
source env/bin/activate
# ---------------------------------------------------
pip install django gunicorn
# ---------------------------------------------------
django-admin startproject restrauntify ~/restrauntify
# ---------------------------------------------------
~/restrauntify/manage.py makemigrations
# ---------------------------------------------------
~/restrauntify/manage.py migrate
# ---------------------------------------------------
sudo ufw allow 8000
# ---------------------------------------------------
~/restrauntify/manage.py runserver 0.0.0.0:8000
# ---------------------------------------------------
gunicorn --bind 0.0.0.0:8000 restrauntify.wsgi
# ---------------------------------------------------
deactivate
# ---------------------------------------------------
sudo vim /etc/systemd/system/gunicorn.socket
# ---------------------------------------------------
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
# ---------------------------------------------------
sudo vim /etc/systemd/system/gunicorn.service
# ---------------------------------------------------
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=tanishq
Group=www-data
WorkingDirectory=/home/tanishq/restrauntify
ExecStart=/home/tanishq/restrauntify/env/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          restrauntify.wsgi:application

[Install]
WantedBy=multi-user.target
# ---------------------------------------------------
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
# ---------------------------------------------------
server {
    listen 80;
    server_name www.codewithharry.in;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/harry/projectdir;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
# ---------------------------------------------------
sudo ln -s /etc/nginx/sites-available/textutils /etc/nginx/sites-enabled/
# ---------------------------------------------------
sudo systemctl restart nginx
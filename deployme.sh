#!/bin/bash

server_address="tanishq@64.227.160.102"
password="MyPass@12345"

sshpass -p "$password" ssh -tt "$server_address" <<EOF 
    cd ./restrauntify 
    git pull origin main 
    cd ./server_main/ 
    . /home/tanishq/restrauntify/server_main/env/bin/activate 
    pip3 install -r requirements.txt
    python3 manage.py makemigrations
    python3 manage.py migrate
    echo "$password" | sudo -S systemctl restart gunicorn
EOF
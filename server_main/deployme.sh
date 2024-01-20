sshpass -p "MyPass@12345" ssh "tanishq@64.227.160.102" <<EOF 
    cd ./restrauntify 
    git pull origin main 
    cd ./server_main/ 
    source ./env/bin/activate 
    pip3 install -r requirements.txt
    python3 manage.py makemigrations
    python3 manage.py migrate
    sudo systemctl restart gunicorn
EOF
server_address="tanishq@64.277.160.102"
password="MyPass@12345"

sshpass -p "$password" ssh "$server_address" <<EOF 
    cd ./restrauntify 
    git pull origin main 
    cd ./server_main/ 
    source ./env/bin/activate 
    pip3 install -r requirements.txt
    python3 manage.py makemigrations
    python3 manage.py migrate
    echo "$password" | sudo -S systemctl restart gunicorn
EOF
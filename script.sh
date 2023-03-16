# database
sudo docker build -t moisesdias/mydb:2.0 ./database
sudo docker push moisesdias/mydb:2.0

kubectl apply -f ./database/db-deployment.yml

# backend
sudo docker build -t moisesdias/mybackend:2.0 ./backend
sudo docker push moisesdias/mybackend:2.0

kubectl apply -f ./backend/backend-deployment.yml

# frontend
sudo docker build -t moisesdias/myfront:2.0 ./frontend
sudo docker push moisesdias/myfront:2.0

kubectl apply -f ./frontend/frontend-deployment.yml



# pegar o ip dando minikube service

# colocar o ip no front e acessar o index.html

# salvar uns dados e dar um
# kubectl exec --tty --stdin mysql-7c9454dc8f-bdlk4 -- /bin/bash

# mysql -u root -h 127.0.0.1 -p
# dar a senha Senha123
# Docker-DjangoCRUD-PostgreSQL-pgAdmin
## Start:

docker-compose run web python manage.py migrate

docker-compose up -d

## you can Access on:

localhost:80 for CRUD

localhost:85 for pgAdmin

## pgAdmin4:

username : admin@gmail.com

password : admin

 Can be adjusted according to the configuration in docker-compose
 
## Connect with Database:

on pgAdmin create server and fill:

database name: postgres

user : postgres

password: postgres


 Can be adjusted according to the configuration in docker-compose
 


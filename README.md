Docker Django MySQL Demo
========================

A very simplistic demo of composing MySQL and Django containers.


    $ git clone https://github.com/dakrauth/docker-django-mysql.git
    $ cd docker-django-mysql
    $ docker-compose up -d db
    $ docker-compose exec db mysql -u root -p -e 'CREATE DATABASE `ddm` DEFAULT CHARACTER SET = `utf8mb4`'
    $ docker-compose up -d app
    $ docker-compose exec app python manage.py createsuperuser


Browse to [http://localhost:9000](http://localhost:9000)
docker-compose exec app python manage.py makemigrations apptest
docker-compose exec app python python manage.py migrate
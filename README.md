Intruncciones Backend Test: Desafío Envíame
========================

Siga los siguientes pasos para ejecutar el proyecto en local.


    $ git clone https://github.com/machahui/backend-test.git
    $ cd backend-test
    $ docker-compose up -d db
    $ docker-compose exec db mysql -u root -p -e 'CREATE DATABASE `ddm` DEFAULT CHARACTER SET = `utf8mb4`'
    $ Ingrese contraseña "root"
    $ docker-compose up -d app
    $ docker-compose exec app python manage.py createsuperuser
    $ docker-compose exec app python manage.py makemigrations apptest    
    $ docker-compose exec app python manage.py migrate


Ingresar a: [http://localhost:9000](http://localhost:9000)
El ejercicio 2 se encuentra en el directorio apptest (model,serializer,urls,views)

Los ejercicios 3,4,5,6 y 7 se encuentra en el archico apptest/ejecicios.py

Intruncciones Backend Test: Desafío Envíame
========================

Siga los siguientes pasos para ejecutar el proyecto en local(ejercicio1).


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
    
    -Para ingresar registros con Faker llamé al método get http://localhost:9000/empresa/generateregistrosempresas
    -Para ver las direcciones del CRUD ingrese a apptest/urls.py

Los ejercicios 3,4,5,6 y 7 se encuentran en el archivo apptest/ejecicios.py, para ejecutar realizar lo siguiente.
    
    $ docker-compose exec app pip install requests (solo para regularizar, en caso ya levanto el servicio docker)
    $ python3 apptest/ejercicios.py ejercicio3
    $ python3 apptest/ejercicios.py ejercicio4
    $ python3 apptest/ejercicios.py ejercicio5
    $ python3 apptest/ejercicios.py ejercicio6
    $ python3 apptest/ejercicios.py ejercicio7


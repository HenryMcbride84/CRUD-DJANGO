# CRUD_app

------------------------------------------------
Paquetes Instalados (Dentro del entorno virtual)

     django           -- Framework (MVT)
     psycopg2-binary  -- Adapter PostgreSQL
     python-decouple  -- Configuración segura
     

Paso 1: Crear entorno virtual

     python3 -m venv venv

Paso 2: Activar el entorno virtual

     source venv/bin/activate

Paso 3: Instalar paquetes

     pip install -r requirements.txt

Paso 4: Crear archivo .env

     touch .env

Paso 5: Crear un archivo .env para los parametros de la base datos

     SECRET_KEY= 'django-insecure-q$ly_5b09fa%#e_@@qj6ww$7uln*dn_ye&mx8x10u_web1ne@f'
     DB_NAME= ''
     DB_USER= ''
     DB_PASSWORD= ''
     DB_HOST= ''
     DB_PORT= ''

Paso 6: Ejecutar la aplicación

     python3 manage.py runserver 8000

------------------------------------------------
Restaurar la base de datos


Paso 1: Copiar el respaldo spmex_db010426.sql al directorio de postgres

     sudo cp spmex_db010426.sql /var/lib/postgresql

Paso 2: Cambiar los permisos de propietario a postgres(usuario sistema operativo)

     sudo chown postgres:postgres spmex_db010426.sql

Paso 3:Dentro del cliente psql crear usuario y base de datos

     CREATE USER spmex_user WITH PASSWORD 'spmex_user';
     CREATE DATABASE spmex_db OWNER spmex_user;

Paso 4: Restaurar la base de datos con el cliente psql(usuario postgres)

     psql -U spmex_user -d spmex_db -f spmex_db010426.sql

Paso 5: Ejecutar migraciones django a nuestro cluster(dentro entorno virtual)

     python manage.py makemigrations
     python manage.py migrate
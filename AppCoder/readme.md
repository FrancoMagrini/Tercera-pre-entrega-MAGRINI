### TERCERA PRE ENTREGA  - MAGRINI, Franco
# PROYECTO COMPLEJO DEPORTIVO



## Instrucciones instalar proyecto en local
+ Crea una carpeta contenedora madre
+ Abre la consola y ubicate en la carpeta madre
+ Crea y activa el ambiente virtual
+ Clona este proyecto en la carpeta madre
+ Entra en la carpeta que acabas de clonar
+ Para instalar las dependencias corre este comando:

```
pip install -r requirements.txt
```
+ El trabajo corre con la base de datos sqlite y que para que corra bien el programa, antes de ejecutar: 

```
python manage.py runserver 
```
+ Se debe ejecutar:
```
python manage.py migrate
```

+ Acceder a la página
```
127.0.0.1:8000
```
# El proyecto cuenta con las siguientes rutas
+ admin
+ crear_perro
+ listar_perros
+ crear_adoptante
+ listar_adoptantes
+ crear_adopcion
+ listar_adopcion
+ buscar_perros
+ error
+ error-2
+ error_creacion_adoptante
+ felicitaciones-adopcion
+ eliminar-adoptante
+ eliminar-perro
+ editar-perro
+ ver-mas
+ perfiles
+ about

## Acerca del proyecto
+ El proyecto es una página de un complejo deportivo que tiene canchas de PADEL y FUTBOL y que permite la registración de usuarios al complejo, la reserva de canchas de padel, la reserva de canchas de futbol y buscar la disponibilidad de canchas de padel (en este caso).

+ Ingresnado a la pagina tiene los accesos "USUARIOS", "DISPONIBILIDAD PADEL", "RESERVAS PADEL" y "RESERVAS FUTBOL".

+ Desde RESERVAS FUTBOL se podrá seleccional el día y la hora allí sin estar logueado solo podrá ingresar al apartado "ver más" de cada perro e ingresar al "acerca de" y buscar perros por tamaño. Ya una vez registrado y logueado podrá crear un perro.
+ También podrá editar o eliminar sus propios canes.
+ Si selecciona "Agregar perro", lo enviará a loguearse y le saldrá el formulario para Agregarlo, una vez agregado lo redireccionará a la lista de perros.
+ Si selecciona el otro campo "Buscar perro por tamaño" debe ingresar (chico,mediano o grande, o VER TODOS) 
y le filtrará en la lista los perros para adoptar según el tamaño que haya seleccionado.
+ El otro apartado en la página es "Crearme como adoptante" donde también debe estar logueado para hacerlo
y una vez allí le sale el formulario para crearse como adoptante.
+ Una vez creado lo envía al apartado adoptar donde podrá seleccionar entre los perros de la lista y de adoptante a Ud mismo, no podrá ver a los demás adoptantes por cuestiones privadas.
+ Finalmente puede acceder a "Acerca de" para ver la información del creador de la página.

## Superuser y Password
Superuser: admin
Password: admin
email: admin@admin.com
ruta: admin/

+ Desde el panel administrativo usted podrá realizar todas las acciones que hace un usuario logueado y podrá manejar los datos de todos los modelos del proyecto.
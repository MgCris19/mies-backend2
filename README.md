# MIES_UG_BACKEND_PRODUCCION
Proyecto desarrollado con Django usando microservicios

# Estandar
project name: app_mies
superuser: 
	name: mies
	password: mies
	email: mies@ug.edu.ec
-------------Estandar response
ok          -> '0000'
erro_bd     -> '9999'
bad_request -> '0400'
not_found   -> '0404'
internal_e  -> '0500'
created     -> '0201'
UNAUTHORIZED-> '0401'
conflict    -> '0409'

---------------------
## Pasos para preparar el ambiente
1. Crear una carpeta que contendrá tu proyecto ***(ej: proyecto_mies)***
2. Abrir el `cmd` de la carpeta
3. Escribir los siguiente comandos en el orden que se detallan  
    **pip install virtualenv**  
    **virtualenv env**  
    **cd env**  
    **cd scripts**  
    **activate**  

## Pasos para clonar el proyecto
4. Entrar a la carpeta creada en el paso 1 ***(proyecto_mies)***
5. Abrir el `cmd` de la carpeta
6. Escribir lo siguiente
    **git clone https://github.com/ProyectoMiesBackEnd/MIES_UG_BACKEND_PRODUCCION.git**

## Pasos para levantar el proyecto
7. Ahora tendras lo siguiente dentro de tu carpeta ***(proyecto_mies)***  
    **env**  
    **MIES_UG_BACKEND_PRODUCCION**  
8. Abrir el `cmd` de la carpeta  
9. Escribir los siguientes comandos 
    **cd env**  
    **cd scripts**  
    **activate**    
    Ahora tendras algo así en tu `cmd`  
    **(env) C:...\proyecto_mies\env\Scripts>**  
10. Regresar a la raíz    
    **(env) C:...\proyecto_mies>**  
11. Ir a la carpeta del proyecto que clonó en el paso 6  
    **(env) C:..\proyecto_miess\MIES_UG_BACKEND_PRODUCCION>**  
12. Escribir el siguiente comando para que se instalen todos los módulos necesarios  
    **pip install -r requirements.txt**  
13. Abrir el visutal code con el siguiente comando  
    **code .**  
14. Limpiar el `cmd`  
    **cls**
15. Levantar el proyecto  
    **python manage.py runserver**



# Lo mismo que arriba pero más feo  
-----------------
1. instalar ambiente virtual  
	pip install virtualenv  
2. crear ambiente  
	virtualenv env  
3. activar ambiente  
	cd env  
	cd scripts  
		activate  
4. activar django (regresar a la raiz)  
	pip install -r requirements.txt  
5. crear el proyecto (core <- standar)  
	django-admin startproject core .  
6. levantar el servidor  
	python manage.py runserver  

------instalaciones
pip install django-simple-history
pip install drf-yasg

------- 
7. crear migraciones
	python manage.py makemigrations
	python manage.py migrate
8. crear un superusuario
	python manage.py createsuperuser

---- carpeta que engloba los proyectos
9. crear el proyecto 
    python manage.py startapp modelBase
	python manage.py startapp student
	python manage.py startapp observations
	python manage.py startapp economyActivity	
	python manage.py startapp user
	python manage.py startapp userProfile
	python manage.py startapp entrepreneur
	python manage.py startapp logGeneral
	python manage.py startapp bond
	python manage.py startapp miesStorageValidated
	python manage.py startapp entrepreneurShip
	python manage.py startapp login
	python manage.py startapp middleware
	


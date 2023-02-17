CONEXION_NAME = 'db_mies_DEV'
CONEXION_USER = 'root'
CONEXION_PASSWORD = 'C097_gXyf-2807676'
CONEXION_HOST = '164.92.85.40'
CONEXION_PORT = 3306

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': CONEXION_NAME,
        'USER': CONEXION_USER,
        'PASSWORD': CONEXION_PASSWORD,
        'HOST': CONEXION_HOST,
        'PORT': CONEXION_PORT,
	'OPTIONS': {
        'init_command': 'SET default_storage_engine=INNODB'
    	}
    }
}

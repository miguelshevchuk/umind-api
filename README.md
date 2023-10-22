# UMind-api

UMind-api es un servicio backend desarrollado en Python, que sirve para analizar los Dibujos y realizar una clasificacion de indicadores emocionales.


## Estructura del proyecto

Para cumplir el objetivo, este proyecto tiene 4 archivos a tener en cuenta:

**modelUmind.pt:** Este archivo es el modelo entrenado, que se utilizada para detectar las distintas partes del dibujo que se utilizaran para su posterior clasificacion  
**model_controller.py:** Este archivo contiene la logica correspondiente a la utilizacion del modelo, y el ordenamiento de los datos para poder luego clasificarlos  
**cloudinary_controller.py:** Este archivo contiene la logica que corresponde a la subida del dibujo a Cloudinary (En caso de utilizar la opcion de analisis de la imagen en base64)  
**indicadores_controller.py:** Este archivo contiene la clasificacion de indicadores

## Instalacion

### Prerequisitos

Usted necesita tener Python 3 instalado en su PC para poder levantar este proyecto

### Preparacion del ambiente

Se debe generar un espacio virtual de Python para levantar el proyecto. Ejecute los siguientes comandos en la terminal desde la _raiz_ del proyecto
```bash
python -m venv ./venv
. ./venv/bin/activate
```
### Instalacion de dependencias

Para instalar las dependencias del proyecto, ejecute el siguiente comando en la terminal

```bash
pip install -r requirements.txt
```

### Levantar aplicacion

Para levantar la aplicacion, ejecute el siguiente comando en la terminal desde la _raiz_ del proyecto

```bash
python app.py
```

Una vez ejecutado el comando, la aplicacion estara disponible en la url "_http://127.0.0.1:5000_"

## Pruebas

### Endpoints

Para poder probar el proyecto, cuenta con 2 endpoints POST que se pueden ejecutar, por ejemplo, desde un PostMan

_http://127.0.0.1:5000/predict_ 

Con este endpoint se podra realizar el analisis, pasando por parametro una imagen en base64

**Request:* 

```bash
{
    "imagen": "IMAGEN_EN_BASE64"
}
```

_http://127.0.0.1:5000/predict/url_ 

Con este endpoint se podra realizar el analisis, pasando por parametro una url de una imagen subida a internet

**Request:* 

```bash
{
    "imagen": "URL_IMAGEN"
}
```

### Cloud

La misma aplicacion, se encuentra disponible en AWS bajo la url _https://api.umind-app.com_
Tenga en cuenta, que por una cuestion de costos, la aplicacion puede no encontrarse levantada en todo momento.

### Datos de prueba

En la _raiz_ del proyecto encontrara un archivo _"urls.txt"_ en donde encontrara distintas url de imagenes para poder realizar las pruebas
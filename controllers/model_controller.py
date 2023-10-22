from ultralytics import YOLO
import cloudinary
import cloudinary.uploader
import random
from os import remove
from controllers.indicadores import indicadores_controller

partes = {0: 'cabeza', 1: 'oreja', 2: 'ojos', 3: 'nariz', 4: 'feliz', 5: 'pierna', 6: 'pie', 7: 'torso', 8: 'mano', 9: 'brazo'}

def predict(img):
    try:
        id=random.randrange(9999999999999999999999999)
        urlImagen = "https://res.cloudinary.com/dgvsnqsq0/image/upload/v1692754492/"+str(id)+".jpg"
        subirImagen(img, id)

        resultados = predecir(urlImagen, str(id)+".jpg")
        return resultados
    except Exception as e:
        print("error")
        print(e)

def predictImgCargada(img):
    try:
        nombreArchivo = img.split("/")
        resultados = predecir(img, nombreArchivo[len(nombreArchivo)-1])
        return resultados
    except Exception as e:
        print("error")
        print(e)

def predecir(img, nombreArchivo):
    modeloEntrenado = "./modelUmind.pt"
    print("URL de la imagen: " + img)
    model = YOLO(modeloEntrenado)
    print("Iniciando prediccion")
    results = model(img)
    resultado = results[0]
    detecciones = armarDetecciones(resultado.boxes)
    remove("./" + nombreArchivo)


    return indicadores_controller.generarIndicadores(detecciones)

def armarDetecciones(boxes):
    print("Armando predicciones")
    predicciones = {
        "mano":[],
        "brazo": [],
        "cabeza": [],
        "oreja": [],
        "ojos": [],
        "nariz": [],
        "feliz": [],
        "pierna": [],
        "pie": [],
        "torso": []

    }
    for box in boxes:
        xyxy = [float(box.xyxy[0][0]), float(box.xyxy[0][1]), float(box.xyxy[0][2]), float(box.xyxy[0][3])]
        anchoDeteccion = float(box.xywh[0][2])
        altoDeteccion = float(box.xywh[0][3])
        clase = partes[int(box.cls[0])]
        prediccion = {
            "xyxy": xyxy,
            "ancho": anchoDeteccion,
            "alto": altoDeteccion,
            "clase": clase
        }
        predicciones[clase].append(prediccion)



    print("Se encontraron: ")
    print("Manos: "+ str(len(predicciones["mano"])))
    print("Brazos: " + str(len(predicciones["brazo"])))
    print("Cabezas: " + str(len(predicciones["cabeza"])))
    print("Orejas: " + str(len(predicciones["oreja"])))
    print("Ojos: " + str(len(predicciones["ojos"])))
    print("Narices: " + str(len(predicciones["nariz"])))
    print("Bocas Felices: " + str(len(predicciones["feliz"])))
    print("Piernas: " + str(len(predicciones["pierna"])))
    print("Pies: " + str(len(predicciones["pie"])))
    print("Torsos: " + str(len(predicciones["torso"])))

    return predicciones


cloudinary.config(
    cloud_name="dgvsnqsq0",
    api_key="511677427851566",
    api_secret="eETyvycX6ldvSjF7N4ml4bnfV1s"
)

def subirImagen(img, id):
    cloudinary.uploader.upload(img, public_id=str(id))


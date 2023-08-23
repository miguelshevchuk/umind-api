from ultralytics import YOLO
import cloudinary
import cloudinary.uploader
import random
from os import remove
from PIL import Image
import cv2


def predict(img):
    modeloEntrenado = "./modelUmind.pt"
    try:
        id=random.randrange(9999999999999999999999999)
        urlImagen = "https://res.cloudinary.com/dgvsnqsq0/image/upload/v1692754492/"+str(id)+".jpg"
        subirImagen(img, id)
        print("URL: "+urlImagen)
        model = YOLO(modeloEntrenado)
        print("Encontre model")
        results = model(urlImagen)
        print(results)
        remove("./"+str(id)+".jpg")
        #return results
    except Exception as e:
        print("error")
        print(e)




cloudinary.config(
    cloud_name="dgvsnqsq0",
    api_key="511677427851566",
    api_secret="eETyvycX6ldvSjF7N4ml4bnfV1s"
)

def subirImagen(img, id):
    cloudinary.uploader.upload(img, public_id=str(id))
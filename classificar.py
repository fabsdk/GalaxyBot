import tensorflow as tf
from tensorflow import keras
import requests
from PIL import Image
from io import BytesIO
import numpy as np
import cv2
import os

def formatarImagem(image):
    image = cv2.resize(image, (170, 170))
    image = image.reshape((1, 170, 170, 3,))
    image = tf.cast(image/255. ,tf.float32)

    return image

def prediction(imagem):
    request = requests.get(imagem)

    image = Image.open(fp=BytesIO(request.content))
    image = image.convert('RGB')

    arr_image = np.array(image)

    image = formatarImagem(arr_image)

    # Carregar modelo
    model = tf.keras.saving.load_model("modelPlanets-MoonsData.h5")

    prediction = model.predict([image])
    if prediction[0].max() == prediction[0][0]:
        return "Esta me parece a Terra! "
    elif prediction[0].max() == prediction[0][1]:
        return "Este me parece Jupiter!"
    elif prediction[0].max() == prediction[0][2]:
        return "Este me parece o Makemake, como você conhecia esse cara aqui?!"
    elif prediction[0].max() == prediction[0][3]:
        return "Este me parece Marte!"
    elif prediction[0].max() == prediction[0][4]:
        return "Este me parece Mercurio!"
    elif prediction[0].max() == prediction[0][5]:
        return "Esta me parece a Lua!"
    elif prediction[0].max() == prediction[0][6]:
        return "Este me parece Netuno!"
    elif prediction[0].max() == prediction[0][7]:
        return "Este me parece Plutão e o coitado nem é mais planeta :("
    elif prediction[0].max() == prediction[0][8]:
        return "Este me parece Saturno!"
    elif prediction[0].max() == prediction[0][9]:
        return "Este me parece Urano!"
    elif prediction[0].max() == prediction[0][10]:
        return "Este me parece Venus!"

import base64
import cv2
import numpy as np
import pandas as pd
from keras.models import model_from_json

def prediction(base64Picture):
    json_file = open('model2.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    best_model = model_from_json(loaded_model_json)
    images = []
    labels = []
    shape = (128, 128)
    source = base64.b64decode(base64Picture[0])
    npimg = np.fromstring(source, dtype=np.uint8);
    img = cv2.imdecode(npimg, 1)
    labels.append(1)
    img = cv2.resize(img, shape)
    images.append(img)
    images = np.array(images) / 255
    predictions = best_model.predict(images)
    predictions = pd.DataFrame(predictions, columns=['Nicht-MM', 'MM'])
    return str(predictions['MM'][0])

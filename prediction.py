import base64
import cv2
import numpy as np
import pandas as pd
from keras.models import model_from_json
from tensorflow import keras


def prediction(base64Picture):
    images = []
    shape = (128, 128)
    # Load Model
    json_file = open('model5.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    best_model = model_from_json(loaded_model_json)
    # load weights into new model
    best_model.load_weights("model5.h5")
    opt = keras.optimizers.Adam(learning_rate=1e-05)
    best_model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=['acc'])
    # Prepare Image
    source = base64.b64decode(base64Picture[0])
    npimg = np.fromstring(source, dtype=np.uint8);
    img = cv2.imdecode(npimg, 1)
    img = cv2.resize(img, shape)
    images.append(img)
    images = np.array(images) / 255
    # Prediction
    predictions = best_model.predict(images)
    predictions = pd.DataFrame(predictions, columns=['Nicht-MM', 'MM'])
    print(predictions)
    return str(predictions['MM'][0])

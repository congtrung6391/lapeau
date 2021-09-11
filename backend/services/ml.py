import numpy as np
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import backend as K
from PIL import Image
import tensorflow as tf
import random
import matplotlib.pyplot as plt
import os
import yaml
import shutil
import seaborn as sns
from keras.models import load_model
from keras.preprocessing import image
import matplotlib.pyplot as plt

from flaskr.record import Record
from flaskr.recorddetail import Recorddetail

img_size = 456
batch_size = 16

IMG_SHAPE = shape=(img_size, img_size, 3)

# base_model = tf.keras.applications.EfficientNetB1(input_shape=IMG_SHAPE, include_top=False, weights='imagenet', drop_connect_rate=0.4)
# base_model.trainable = True

# inputs = tf.keras.Input(IMG_SHAPE)
# x = base_model(inputs, training=True)
# x = tf.keras.layers.GlobalAveragePooling2D()(x)
# x = tf.keras.layers.Dropout(0.5)(x)
# #x = tf.keras.layers.Dense(256, activation='relu')(x)
# #x = tf.keras.layers.Dense(128, activation='relu')(x)
# #x = tf.keras.layers.Dense(64, activation='relu')(x)
# x = tf.keras.layers.Dense(32, activation='relu')(x)
# outputs = tf.keras.layers.Dense(4, activation='softmax')(x)
# model = tf.keras.Model(inputs, outputs)

def f1_score(y_true, y_pred): #taken from old keras source code
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    recall = true_positives / (possible_positives + K.epsilon())
    f1_val = 2*(precision*recall)/(precision+recall+K.epsilon())
    return f1_val


model = tf.keras.models.load_model('my_model.h5', custom_objects={'f1_score': f1_score})

# callback = [tf.keras.callbacks.EarlyStopping(monitor='loss', patience=40)]
# model.compile(optimizer=tf.keras.optimizers.Adam(lr=lr),
#           loss=tf.keras.losses.CategoricalCrossentropy(),
#           metrics=['accuracy', f1_score])


from flask import Blueprint, request, jsonify, json, Response
from datetime import datetime
import base64

bp = Blueprint('ml', __name__, url_prefix='/ml')

def load_image(img_path, show=False):

    img = image.load_img(img_path, target_size=(img_size, img_size))
    img_tensor = image.img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.                                      # imshow expects values in the range [0, 1]

    if show:
        plt.imshow(img_tensor[0])                           
        plt.axis('off')
        plt.show()

    return img_tensor

@bp.route('detect', methods=['POST'])
def detect():
  print(request.is_json)
  
  imageData = request.json['img']
  # print(imageData)

  # imageData = request.form['img']
  print('image received')
  # print(imageData)

  img_path='image.jpg'

  with open(img_path, "wb") as fh:
    fh.write(base64.b64decode(imageData))
  print('image saved')

  # if (len(request.files) == 0):
  #   return "Request not contains a image", 400
  
  # img = request.files['image']

  # print(img)

  # if not img:
  #   return "Request not contains a image", 400
  
  # # img.save(img_path)
  new_image = load_image(img_path)
  print('predicting')
  pred = model.predict(new_image)
  print(pred)
  
  pred = pred.tolist()
  responseData = {
    '0': round(pred[0][0]*100, 2),
    '1': round(pred[0][1]*100, 2),
    '2': round(pred[0][2]*100, 2),
    '3': round(pred[0][3]*100, 2)
  }

  # responseData = {
  #   '0': 1,
  #   '1': 2,
  #   '2': 3,
  #   '3': 4
  # }

  id_record = Record.generate_id()
  username = 'user01'
  image_url = 'cdcdc.cdsc'
  createdAt = datetime.now().strftime("%H:%M:%S")
  isExisted = Record.get(id_record)
  print(isExisted)
  if not isExisted:
    Record.create(
      id_=id_record, username=username, image_url=image_url, createdAt=createdAt
    )
  
  for i in range(4):
    result = responseData[str(i)]
    id_detail = Recorddetail.generate_id()
    if not Recorddetail.get(id_detail):
      Recorddetail.create(
        id_=id_detail, id_sickness=str(i), id_record=id_record, result=result
      )

  return responseData, 200
import tensorflow as tf
import numpy as np
import cv2



def model_nn():
    model = tf.keras.sequential()
    model.add(
        model=tf.keras.layer.Dense(32,input_shape =(10,),activation = 'relu')
    )
    model.add(
        model=tf.keras.layer.Dense(32, input_shape=(10,), activation='relu')
    )
    model.add(
        model=tf.keras.layer.Dense(32, input_shape=(10,), activation='relu')
    )
    model.add(
        model=tf.keras.layer.Dense(32, input_shape=(10,), activation='relu')
    )
    model.add(
        model=tf.keras.layer.Dense(32, input_shape=(10,), activation='relu')
    )
    model.add(
        model=tf.keras.layer.Dense(2, input_shape=(10,), activation='softmax')
    )
    sgd =optimizers.SGD(lr= 0.001)
    model.compile(optimizer = sgd, loss = 'categorical_crossentropy')

    return model


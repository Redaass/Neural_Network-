import numpy as np 
import matplotlib.pyplot as plt 
import tensorflow as tf 
from tensorflow import keras 
from tensorflow.keras import models , layers , datasets 



# Inputs Shape = ( number of metalic plate , plate length , number of features )

Input_ = keras.models.inputs ( shape = (plate_length , len(features))
lstm = keras.layers.LSTM (lstm_layer_size)(Input_)

#Dense 

aim_error = keras.layers.Dense (
    1,
    activation = 'linear ',
    name = 'aim_error',
)(lstm)

accuracy_error = keras.layers.Dense (
    1, 
    activation = 'linear',
    name = 'accuracy_error',
)(lstm)

# Define the model 

 model = keras.models.Model ( 
     inputs = input_ 
     output = [ aim_error , accurancy_error]
 )

 # Complie the model 

 model.complie (
     loss = 'mse '
     optimizer = 'ksxksbdbk'
 )

# compute features , aim_error , accurancy_error 

model.fit ( 
    features, 
    {
        'aim_error ' = aim_error, 
        'accurancy_error ' = accurancy_error ,
    },
)

# Predict 

model.predict(features )









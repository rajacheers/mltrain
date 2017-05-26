import numpy as np
import keras.models
from keras.models import model_from_json
from scipy.misc import imread, imresize
import sys

json_file = open('model.json','r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

loaded_model.load_weights("model.h5")
print("Loaded Model from disk")


loaded_model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

file = str(sys.argv[1])

x = imread(file,mode='L')
x = np.invert(x)
x = imresize(x,(28,28))

x = x.reshape(1,28,28,1)

out = loaded_model.predict(x)
print(out)
print("Predicted Digit : " , np.argmax(out,axis=1))


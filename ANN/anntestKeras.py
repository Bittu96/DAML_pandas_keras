from keras.models import Sequential
from keras.layers import Dense
import numpy
from ann_visualizer.visualize import ann_viz;
from numpy import *

numpy.random.seed(7)

X = array([
[0,1,0,1],
[1,1,0,1],
[0,1,0,1],
[1,1,0,1]])

Y = array([
[0,1],
[1,1],
[1,1],
[0,1]])

# create model
model = Sequential()
model.add(Dense(6, input_dim=4, activation='relu'))
model.add(Dense(2, activation='sigmoid'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X, Y, epochs=90, batch_size=100)
# evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

ann_viz(model, title="Robot Arm");
predictions = model.predict(X)
# round predictions
rounded = [round(x[0]) for x in predictions]
print(rounded)
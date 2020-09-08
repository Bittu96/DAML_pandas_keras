# Create your first MLP in Keras
from keras.models import Sequential
from keras.layers import Dense
import numpy
from ann_visualizer.visualize import ann_viz;
# fix random seed for reproducibility
numpy.random.seed(7)
# load pima indians dataset
dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:3]
Y = dataset[:,8]
# create model
model = Sequential()
model.add(Dense(8, input_dim=3, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X, Y, epochs=10, batch_size=10)
# evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
ann_viz(model, title="Differential Bot");
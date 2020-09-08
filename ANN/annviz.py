import keras;
from keras.models import Sequential;
from keras.layers import Dense;
from ann_visualizer.visualize import ann_viz;

network = Sequential();
        #Hidden Layer#1
network.add(Dense(units=6,
                  activation='relu',
                  kernel_initializer='uniform',
                  input_dim=3));

        #Exit Layer
network.add(Dense(units=2,
                  activation='sigmoid',
                  kernel_initializer='uniform'));

ann_viz(network, title="oneLeggedBot");

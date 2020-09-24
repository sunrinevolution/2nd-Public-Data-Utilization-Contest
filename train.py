
import datetime
import pandas as pd
# import tensorflow as tf
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Dropout, BatchNormalization, LeakyReLU
# from tensorflow.keras.optimizers import SGD

# check tensorflow version
# print(tf.__version__)

# 독립변수: 책 카테고리
# 종속변수: 개표 통계

X_data = pd.read_csv("./data/book_preprocessed/preprocessed_guro.csv") # preprocessed guro book reservation dataset
y_data = pd.read_csv('./data/vote_preprocessed/vote_guro.csv') # preprocessed guro vote dataset

# feature engineering
print(X_data['대출일'])


# build model
# def build_model(X_shape: int = 0) -> Sequential:
#   model = Sequential()
  
#   model.add(Dense(50, input_shape = (X_shape, )))
#   model.add(BatchNormalization())
#   model.add(LeakyReLU(alpha=0.1))
#   model.add(Dropout(0.2))
#   model.add(Dense(50))
#   model.add(BatchNormalization())
#   model.add(LeakyReLU(alpha=0.1))
#   model.add(Dropout(0.2))
#   model.add(Dense(50))
#   model.add(BatchNormalization())
#   model.add(LeakyReLU(alpha=0.1))
#   model.add(Dropout(0.2))
#   model.add(Dense(50))
#   model.add(BatchNormalization())
#   model.add(LeakyReLU(alpha=0.1))
#   model.add(Dropout(0.2))
#   model.add(Dense(10))
#   model.add(LeakyReLU(alpha=0.1))
  
#   sgd = SGD(lr = 0.001)
#   model.compile(optimizer = sgd, loss = 'categorical_crossentropy', metrics = ['accuracy'])

#   return model

# model = build_model(X_data[0].shape)
# history = model.fit(X_train, y_train, validation_split = 0.3, epochs = 100, verbose = 0)


# plt.plot(history.history['acc'])
# plt.plot(history.history['val_acc'])
# plt.legend(['training', 'validation'], loc = 'upper left')
# plt.show()

# results = model.evaluate(X_test, y_test)

# print('Test accuracy: ', results[1])

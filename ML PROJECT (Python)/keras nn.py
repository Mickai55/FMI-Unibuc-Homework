from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
from glob import glob
import time
import librosa as lr
from copy import deepcopy
from sklearn.metrics import confusion_matrix
start = time.time()

train = glob('E:/Informatica/ML proiect/train/train/*.wav') # array with paths to train files (8000)
validation = glob('E:/Informatica/ML proiect/validation/validation/*.wav') # array with paths to train files (1000)
test = glob('E:/Informatica/ML proiect/test/test/*.wav')

train_labels = np.loadtxt('E:/Informatica/ML proiect/train_sorted_labels.txt')
train_labels = np.array(train_labels, dtype = np.int)

validation_labels = np.loadtxt('E:/Informatica/ML proiect/validation_sorted_labels.txt')
validation_labels = np.array(validation_labels, dtype = np.int)

def transformation(file_name):
    audio, sample_rate = lr.load(file_name, res_type='kaiser_fast') 
    arr = lr.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=128)
    final_scaled = np.mean(arr.T, axis=0)

    return final_scaled

# ------------ HARDCODE TABLE
NR_TRAIN = 100
NR_VALIDATION = 100
EPOCHS = 100
# -----------------------------

train_audio = [] # array with audio values for train files
validation_audio = [] # array with audio values for validation files

for i in range(NR_TRAIN):
    mfcc = transformation(train[i])
    train_audio.append(mfcc)

for i in range(NR_VALIDATION):
    mfcc = transformation(validation[i])
    train_audio.append(mfcc)
    validation_audio.append(mfcc)

test_audio = []
print(test[2])  #E:/Informatica/ML proiect/test/test\300003.wav
for i in range(3000):
    mfcc = transformation(test[i])
    test_audio.append(mfcc)

X = np.array(train_audio)
y = np.array(train_labels[:NR_TRAIN])

y = np.append(y, validation_labels[:NR_VALIDATION])

validation_labels = np.array(validation_labels)
validation_audio = np.array(validation_audio)
test_audio = np.array(test_audio)


model = Sequential()
model.add(Dense(12, input_dim=128, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# fit the keras model on the dataset
model.fit(X, y, epochs=EPOCHS, batch_size=10, verbose=1) # , verbose=0

_, accuracy = model.evaluate(X, y, verbose=1) # verbose=0
print('Accuracy: %.2f' % (accuracy*100))

predictions = model.predict(test_audio)

predictions = [int(round(x[0])) for x in predictions]

print(len(predictions))
print(predictions)

print("Time elapsed:", time.time() - start, "seconds.")



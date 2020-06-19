from timeit import default_timer as timer
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob
import librosa as lr

from sklearn import svm
from sklearn.metrics import confusion_matrix

start = timer()

def transform_wav(audio, sfreq):
    audio = np.flip(audio)
    audio = np.asfortranarray(audio)
    lr.output.write_wav('file_trim_22225s.wav', audio, sfreq)

def create_hash_table(dict, path):
    labels = open(path, 'r')
    for line in labels.readlines():
        string = ''
        sw = False
        for i in range(len(line)):
            if line[i] == ',':
                sw = True
            if sw == False:
                string += line[i]
            else:
                dict[string] = line[i + 1]
                break

def display_sound(audio, time):
    fig, ax = plt.subplots()
    ax.plot(time, audio)
    ax.set(xlabel = "Time(s)", ylabel = "Sound amplitude")
    plt.show()


class KNN():
    def __init__(self, train_images, train_labels):
        self.train_images = train_images
        self.train_labels = train_labels

    def classify(self, test_image, n_neighbors = 3):
        distances = np.sqrt(
            np.sum(
                np.square(self.train_images - test_image),
                axis = 1
            )
        )
        neighbors = self.train_labels[
            np.argsort(distances)[:n_neighbors]
        ]
        return np.argmax(np.bincount(neighbors))

def transformation(file_name):
    audio, sample_rate = lr.load(file_name, res_type='kaiser_fast') 
    arr = lr.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=128)
    final_scaled = np.mean(arr.T, axis=0)

    return final_scaled


train = glob('E:/Informatica/ML proiect/train/train/*.wav') # array with paths to train files (8000)
validation = glob('E:/Informatica/ML proiect/validation/validation/*.wav') # array with paths to train files (1000)

train_labels = np.loadtxt('E:/Informatica/ML proiect/train_sorted_labels.txt')
train_labels = np.array(train_labels, dtype = np.int)
# print(train_labels[:10])

validation_labels = np.loadtxt('E:/Informatica/ML proiect/validation_sorted_labels.txt')
validation_labels = np.array(validation_labels, dtype = np.int)
# print(validation_labels[:10])

# train_hash = {} # hash table with labels for train files
# create_hash_table(train_hash, 'E:/Informatica/ML proiect/train.txt')
# validation_hash = {} # hash table with labels for validation files
# create_hash_table(validation_hash, 'E:/Informatica/ML proiect/validation.txt')

train_audio = [] # array with audio values for train files
validation_audio = [] # array with audio values for validation files

time = np.arange(22050) / 22050
# time = np.arange(len(audio)) / sfreq

# ------------ HARDCODE TABLE
NR_TRAIN = 8000
NR_VALIDATION = 1000
# -----------------------------
for i in range(NR_TRAIN):
    mfcc = transformation(train[i])
    train_audio.append(mfcc)

for i in range(NR_VALIDATION):
    mfcc = transformation(validation[i])
    validation_audio.append(mfcc)

# i = 0
# file1 = open("E:/Informatica/ML proiect/audio_data.txt")
# for line in file1.readlines():
#     line = [float(i) for i in line.split(",")]
#     train_audio.append(line)
#     i += 1
#     if i == NR_TRAIN:
#         break

# i = 0
# file2 = open("E:/Informatica/ML proiect/validation_data.txt")
# for line in file2.readlines():
#     line = [float(i) for i in line.split(",")]
#     validation_audio.append(line)
#     i += 1
#     if i == NR_VALIDATION:
#         break

print("\n\nTime elapsed(citire): "+str(timer() - start)+" seconds.")

train_audio = np.array(train_audio)
validation_audio = np.array(validation_audio)

predictions = []
knn = KNN(train_audio, train_labels[:NR_TRAIN])

for i in range (len(validation_audio)):
    predictions.append(knn.classify(validation_audio[i]))
# print(predictions)

print(np.mean(predictions == validation_labels[:NR_VALIDATION]))
print(confusion_matrix(validation_labels[:NR_VALIDATION], predictions))

print("\n\nTime elapsed: "+str(timer() - start)+" seconds.")

# 0.635
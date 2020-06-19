from timeit import default_timer as timer
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob
import librosa as lr

from sklearn import svm

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


train = glob('E:/Informatica/ML proiect/train/train/*.wav') # array with paths to train files (8000)
validation = glob('E:/Informatica/ML proiect/validation/validation/*.wav') # array with paths to train files (1000)


train_labels = np.loadtxt('E:/Informatica/ML proiect/train_sorted_labels.txt')
train_labels = np.array(train_labels, dtype = np.int)
# print(train_labels[:10])

validation_labels = np.loadtxt('E:/Informatica/ML proiect/validation_sorted_labels.txt')
validation_labels = np.array(validation_labels, dtype = np.int)
# print(validation_labels[:10])

train_hash = {} # hash table with labels for train files
create_hash_table(train_hash, 'E:/Informatica/ML proiect/train.txt')
validation_hash = {} # hash table with labels for validation files
create_hash_table(validation_hash, 'E:/Informatica/ML proiect/validation.txt')

train_audio = [] # array with audio values for train files
validation_audio = [] # array with audio values for validation files

time = np.arange(22050) / 22050
# time = np.arange(len(audio)) / sfreq

# ------------ HARDCODE TABLE
# NR_TRAIN = 8000
NR_VALIDATION = 1000
# -----------------------------
file = open("E:/Informatica/ML proiect/validation_data.txt", "w")
for i in range(NR_VALIDATION):
    audio, sfreq = lr.load(validation[i])
    file.write(','.join([str(elem) for elem in audio]))
    file.write('\n')

# for i in range(NR_VALIDATION):
#     audio, sfreq = lr.load(validation[i])
#     validation_audio.append(audio)
print("da")
# predictions = []
# knn = KNN(train_audio, train_labels[:NR_TRAIN])

# for i in range (len(validation_audio)):
#     predictions.append(knn.classify(validation_audio[i]))
# # print(predictions)

# print(np.mean(predictions == validation_labels[:NR_VALIDATION]))

print("\n\nTime elapsed: "+str(timer() - start)+" seconds.")

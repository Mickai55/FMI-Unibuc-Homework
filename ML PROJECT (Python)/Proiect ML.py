from timeit import default_timer as timer
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob
import librosa as lr
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix

start = timer()

def transform_to_wav(audio, sfreq):
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

train = glob('E:/Informatica/ML proiect/train/train/*.wav') # array with paths to train files (8000)
validation = glob('E:/Informatica/ML proiect/test/test/*.wav') # array with paths to train files (1000)

train_labels = np.loadtxt('E:/Informatica/ML proiect/train_sorted_labels.txt')
train_labels = np.array(train_labels, dtype = np.int)
# print(train_labels[:10])

# validation_labels = np.loadtxt('E:/Informatica/ML proiect/validation_sorted_labels.txt')
# validation_labels = np.array(validation_labels, dtype = np.int)
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
NR_TRAIN = 60
NR_VALIDATION = 1000
NUM_BINS = 10
# -----------------------------
print(NR_TRAIN)
for i in range(NR_TRAIN):
    audio, sfreq = lr.load(train[i])
    train_audio.append(audio)

for i in range(NR_VALIDATION):
    audio, sfreq = lr.load(validation[i])
    validation_audio.append(audio)

# for NUM_BINS in range(2, 20):
print("NUM_BINS = " + str(NUM_BINS))
bins = np.linspace(start = -0.7, stop = 0.7, num = NUM_BINS)

train_audio = np.digitize(train_audio, bins)
validation_audio = np.digitize(validation_audio, bins)

# for i in range(len(train_audio[0])):
#     print(train_audio[0][i], end = " ")

naive_bayes_model = MultinomialNB()
naive_bayes_model.fit(train_audio, train_labels[:NR_TRAIN])
predictions = naive_bayes_model.predict(validation_audio)

print(predictions)
print(np.sum(predictions == 1))
print(np.sum(predictions == 0))
# print(np.mean(predictions == validation_labels[:NR_VALIDATION]))

# print(confusion_matrix(validation_labels[:NR_VALIDATION], predictions))




print("\n\nTime elapsed: "+str(timer() - start)+" seconds.")



# NR_TRAIN = 8000
# NR_VALIDATION = 1000

# NUM_BINS = 2
# 0.528
# [[  0 472]
#  [  0 528]]
# NUM_BINS = 3
# 0.46
# [[203 269]
#  [271 257]]
# NUM_BINS = 4
# 0.51
# [[240 232]
#  [258 270]]
# NUM_BINS = 5
# 0.475
# [[215 257]
#  [268 260]]
# NUM_BINS = 6
# 0.483
# [[215 257]
#  [260 268]]
# NUM_BINS = 7
# 0.496
# [[226 246]
#  [258 270]]
# NUM_BINS = 8
# 0.485
# [[219 253]
#  [262 266]]
# NUM_BINS = 9
# 0.482
# [[219 253]
#  [265 263]]
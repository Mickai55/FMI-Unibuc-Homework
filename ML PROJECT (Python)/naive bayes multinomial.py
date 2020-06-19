# import wave
# w = wave.open('E:/Informatica/ML proiect/train/train/100001.wav', 'rb')
# for i in range(w.getnframes()):
#     frame = w.readframes(i)
#     print(frame)

# from scipy.io import wavfile
# fs, data = wavfile.read('E:/Informatica/ML proiect/train/train/100001.wav')
# print(fs, data / 22050)

from timeit import default_timer as timer
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob
import librosa as lr
from sklearn.naive_bayes import MultinomialNB
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

train_hash = {} # hash table with labels for train files
create_hash_table(train_hash, 'E:/Informatica/ML proiect/train.txt')
validation_hash = {} # hash table with labels for validation files
create_hash_table(validation_hash, 'E:/Informatica/ML proiect/validation.txt')

train_audio = [] # array with audio values for train files
validation_audio = [] # array with audio values for validation files

time = np.arange(22050) / 22050
# time = np.arange(len(audio)) / sfreq

# ------------ HARDCODE TABLE
NR_TRAIN = 8000
NR_VALIDATION = 1000
# NUM_BINS = 6
# -----------------------------

# file1 = open("E:/Informatica/ML proiect/audio_data.txt")
# for line in file1.readlines():
#     line = [float(i) for i in line.split(",")]
#     train_audio.append(line)

# file2 = open("E:/Informatica/ML proiect/validation_data.txt")
# for line in file2.readlines():
#     line = [float(i) for i in line.split(",")]
#     validation_audio.append(line)

for i in range(NR_TRAIN):
    mfcc = transformation(train[i])
    train_audio.append(mfcc)

for i in range(NR_VALIDATION):
    mfcc = transformation(validation[i])
    validation_audio.append(mfcc)

for NUM_BINS in range(2, 20):
    print("NUM_BINS = " + str(NUM_BINS))
    bins = np.linspace(start = -0.7, stop = 0.7, num = NUM_BINS)

    Xtrain_audio = np.digitize(train_audio, bins)
    Xvalidation_audio = np.digitize(validation_audio, bins)

    # for i in range(len(train_audio[0])):
    #     print(train_audio[0][i], end = " ")

    naive_bayes_model = MultinomialNB()
    naive_bayes_model.fit(Xtrain_audio, train_labels[:NR_TRAIN])
    predictions = naive_bayes_model.predict(Xvalidation_audio)

    # print(predictions)
    print(np.mean(predictions == validation_labels[:NR_VALIDATION]))

    print(confusion_matrix(validation_labels[:NR_VALIDATION], predictions))

print("\n\nTime elapsed: "+str(timer() - start)+" seconds.")


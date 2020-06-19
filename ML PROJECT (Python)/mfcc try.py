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

def extract_features(file_name):
       
    try:
        audio, sample_rate = lr.load(file_name, res_type='kaiser_fast') 
        mfccs = lr.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=128)
        mfccsscaled = np.mean(mfccs.T,axis=0)
        
    except Exception as e:
        print("Error encountered while parsing file: ", file_name)
        return None 
     
    return mfccsscaled


train = glob('E:/Informatica/ML proiect/train/train/*.wav') # array with paths to train files (8000)
validation = glob('E:/Informatica/ML proiect/validation/validation/*.wav') # array with paths to train files (1000)

train_labels = np.loadtxt('E:/Informatica/ML proiect/train_sorted_labels.txt')
train_labels = np.array(train_labels, dtype = np.int)
# print(train_labels[:10])

# validation_labels = np.loadtxt('E:/Informatica/ML proiect/validation_sorted_labels.txt')
# validation_labels = np.array(validation_labels, dtype = np.int)
# # print(validation_labels[:10])

# train_hash = {} # hash table with labels for train files
# create_hash_table(train_hash, 'E:/Informatica/ML proiect/train.txt')
# validation_hash = {} # hash table with labels for validation files
# create_hash_table(validation_hash, 'E:/Informatica/ML proiect/validation.txt')

# train_audio = [] # array with audio values for train files
# validation_audio = [] # array with audio values for validation files

# time = np.arange(22050) / 22050
# time = np.arange(len(audio)) / sfreq

# ------------ HARDCODE TABLE
# NR_TRAIN = 8000
# NR_VALIDATION = 1000
# NUM_BINS = 2000
# -----------------------------

mfcc = extract_features(train[0])

print(mfcc)



# cu magnitudini

#0.57

# Time elapsed: 131.3908712 seconds.
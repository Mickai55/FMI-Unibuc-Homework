from timeit import default_timer as timer
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob
import librosa as lr
from sklearn.metrics import classification_report
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
test = glob('E:/Informatica/ML proiect/test/test/*.wav')


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
# -----------------------------

for i in range(NR_TRAIN):
    mfcc = extract_features(train[i])
    train_audio.append(mfcc)

for i in range(NR_VALIDATION):
    mfcc = extract_features(validation[i])
    validation_audio.append(mfcc)

clf = svm.SVC(C=85000)

clf.fit(train_audio, train_labels[:NR_TRAIN])

predictions = clf.predict(validation_audio)

print("Accuracy: ", np.mean(predictions == validation_labels[:NR_VALIDATION]))
print("Confusion matrix:")
print(confusion_matrix(validation_labels[:NR_VALIDATION], predictions))

print("Predictii de 1:", np.sum(predictions))
print("Predictii de 0:", 1000 - np.sum(predictions))

# plt.matshow(confusion_matrix(validation_labels[:NR_VALIDATION], predictions))
print(classification_report(validation_labels[:NR_VALIDATION], predictions))

# #------

# deTrimis = open("E:/Informatica/ML proiect/testtest.txt", "w")

# test_file = open('E:/Informatica/ML proiect/test.txt')
# test_names = []
# for line in test_file.readlines():
#     nr = line.split(".")[0]
#     nr = nr[1:]
#     while nr[0] == "0":
#         nr = nr[1:]
#     nr = int(nr)
#     l = str(line[:10] + "," + str(predictions2[nr - 1]) + "\n")
#     deTrimis.write(l)
#     print(l)
#     # test_names.append(line)

# print(test_names)

print("\n\nTime elapsed: "+str(timer() - start)+" seconds.")

# 8000 cu 1000    gamma=0.0001, C=2000
# 0.774 cu res_type='kaiser_fast'
# 0.769 fara res_type='kaiser_fast'

# 8000 cu 1000    gamma=0.0001, C=100
# 0.77 cu res_type='kaiser_fast'
# 0.776 fara res_type='kaiser_fast'
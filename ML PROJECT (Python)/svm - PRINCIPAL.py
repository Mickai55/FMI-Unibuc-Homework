from timeit import default_timer as timer
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob
import librosa as lr
from sklearn import svm

# timer
start = timer()

# is getting an array of amplitudes and a frequency and exports a flipped .wav file, used for informational purposes
def transform_wav(audio, sfreq):
    audio = np.flip(audio)      
    audio = np.asfortranarray(audio)
    lr.output.write_wav('file_trim_22225s.wav', audio, sfreq)

# used to visualise sounds with pyplot
def display_sound(audio, sfreq):
    time = np.arange(len(audio)) / sfreq
    fig, ax = plt.subplots()
    ax.plot(time, audio)
    ax.set(xlabel = "Time(s)", ylabel = "Sound amplitude")
    plt.show()

# used to retun scaled mfccs values
def transformation(file_name):

    # making an array with the amplitudes of the audio file
    audio, sample_rate = lr.load(file_name, res_type='kaiser_fast') 

    # applying the librosa mfcc function with a large number of MFCCs to return
    arr = lr.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=128)

    # scaling the matrix
    final_scaled = np.mean(arr.T, axis=0)

    return final_scaled

# lists that get paths to the train, validation and test sets
train = glob('E:/Informatica/ML proiect/train/train/*.wav')
validation = glob('E:/Informatica/ML proiect/validation/validation/*.wav')
test = glob('E:/Informatica/ML proiect/test/test/*.wav')

# lists with the labels of the audio data
# *the lists were sorted so it's easier to verify the data
train_labels = np.loadtxt('E:/Informatica/ML proiect/train_sorted_labels.txt')
train_labels = np.array(train_labels, dtype = np.int)
validation_labels = np.loadtxt('E:/Informatica/ML proiect/validation_sorted_labels.txt')
validation_labels = np.array(validation_labels, dtype = np.int)

train_audio = [] # array with audio values for train files
validation_audio = [] # array with audio values for validation files
test_audio = [] # array with audio values for test files

# ------------ HARDCODE TABLE *used so i can test data with a lower number of train/validation files
NR_TRAIN = 8000
NR_VALIDATION = 1000
# -----------------------------

# making the train list with the features extracted 
for i in range(NR_TRAIN):
    mfcc = transformation(train[i])
    train_audio.append(mfcc)

# appending the validation data to the train data
for i in range(NR_VALIDATION):
    mfcc = transformation(validation[i])
    train_audio.append(mfcc)

# making the test list with the features extracted 
for i in range(3000):
    mfcc = transformation(test[i])
    test_audio.append(mfcc)

# appending the validation labels to the train labels
train_labels = np.append(train_labels, validation_labels)

# making the svm model with C=85000
clf = svm.SVC(C=85000)

# fitting train to the labels
clf.fit(train_audio, train_labels)

# predicting the test data
predictions = clf.predict(test_audio)

# opening the file to be written 
toSend = open("E:/Informatica/ML proiect/testtest.txt", "w")
# opening the file where the names of the test data are
test_file = open('E:/Informatica/ML proiect/test.txt')

# writting names of the test data and the corresponding labels
for line in test_file.readlines():
    nr = line.split(".")[0]
    nr = nr[1:]
    while nr[0] == "0":
        nr = nr[1:]
    nr = int(nr)
    l = str(line[:10] + "," + str(predictions[nr - 1]) + "\n")
    toSend.write(l)

# printing the timer
print("\n\nTime elapsed: "+str(timer() - start)+" seconds.")

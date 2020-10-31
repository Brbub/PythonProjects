import wave
import numpy as np
import matplotlib.pyplot as plt
import sys
import dtw
import librosa

def wav_graph(x,y):
    y1, sr1 = librosa.load(x) 
    y2, sr2 = librosa.load(y) 

    #Showing multiple plots using subplot
    plt.subplot(1, 2, 1) 
    mfcc1 = librosa.feature.mfcc(y1,sr1)   #Computing MFCC values
    librosa.display.specshow(mfcc1)

    plt.subplot(1, 2, 2)
    mfcc2 = librosa.feature.mfcc(y2, sr2)
    librosa.display.specshow(mfcc2)

    dist, cost, path = dtw(mfcc1.T, mfcc2.T)
    print("The normalized distance between the two : ",dist)   # 0 for similar audios 

    plt.imshow(cost.T, origin='lower', cmap=plt.get_cmap('gray'), interpolation='nearest')
    plt.plot(path[0], path[1], 'w')   #creating plot for DTW

    plt.show()

wav_graph('Samples/speak.wav','Samples/out.wav')



'''
def test():
wr = wave.open('Samples/speak.wav', 'r')
# Set the parameters for the output file.
par = list(wr.getparams())
par[3] = 0  # The number of samples will be set by writeframes.
par = tuple(par)
ww = wave.open('Samples/pitch2.wav', 'w')
ww.setparams(par)

fr = 1000
sz = wr.getframerate()//fr  # Read and process 1/fr second at a time.
# A larger number for fr means less reverb.
c = int(wr.getnframes()/sz)  # count of the whole file
shift = 100//fr  # shifting 100 Hz
for num in range(c):
    da = np.fromstring(wr.readframes(sz), dtype=np.int16)
    left, right = da[0::2], da[1::2]  # left and right channel
    lf, rf = np.fft.rfft(left), np.fft.rfft(right)
    lf, rf = np.roll(lf, shift), np.roll(rf, shift)
    lf[0:shift], rf[0:shift] = 0, 0
    nl, nr = np.fft.irfft(lf), np.fft.irfft(rf)
    ns = np.column_stack((nl, nr)).ravel().astype(np.int16)
    ww.writeframes(ns.tostring())
wr.close()
ww.close()
'''
import librosa
import numpy as np

def converter(ifile):
    audio, _ = librosa.load(ifile)
    output = np.abs(librosa.stft(audio))
    return output



    


    
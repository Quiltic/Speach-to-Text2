import pyaudio, os, wave, winsound, numpy, pickle, random
import speech_recognition as sr

import pyautogui, time, keyboard


def save(obj, name ):
    try:
        os.remove(name)
        with open(name, 'wb') as f:
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
    except:
        with open(name, 'wb') as f:
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load(name):
    with open(name, 'rb') as f:
        return pickle.load(f)

#open(PIL)
slow = 0
screenWidth, screenHeight = pyautogui.size()

Programing = False
Key = False
RECORD_SECONDS = 5
Minimum = 600
tally = 0
mute = -1


while True:
    """
    try:
        os.remove('useme.wav')
    except:
        pass
    """
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    #RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "useme.wav"
     
    audio = pyaudio.PyAudio()
     
    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    #winsound.Beep(1000,100)
    #winsound.MessageBeep(winsound.MB_ICONQUESTION)
    #winsound.MB_ICONQUESTION
    print ("Waiting...")
    frames = []

    dirp = 0
    data = stream.read(CHUNK)
    while max(numpy.fromstring(data, dtype=numpy.int16)) < Minimum:
        data = stream.read(CHUNK)

    frames.append(data)
    if mute < 0:
        winsound.Beep(1000,100)
    print ("recording...")
    
    while dirp < 50:
        data = stream.read(CHUNK)
        if max(numpy.fromstring(data, dtype=numpy.int16)) > Minimum:
            mnb = max(numpy.fromstring(data, dtype=numpy.int16))
            print(mnb)
            dirp = 0
        else:
            dirp += 1
        frames.append(data)

        
    #for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    #    data = stream.read(CHUNK)
    #    frames.append(data)
    print ("finished recording")
    if mute < 0:
        winsound.Beep(500,100)
    
    


    #"""
    #winsound.MessageBeep([winsound.MB_OK])
    
     
    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()


#https://www.geeksforgeeks.org/speech-recognition-in-python-using-google-speech-api/
#"""

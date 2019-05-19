#!/usr/bin/env python3
"""Load an audio file into memory and play its contents.

NumPy and the soundfile module (http://PySoundFile.rtfd.io/) must be
installed for this to work.

This example program loads the whole file into memory before starting
playback.
To play very long files, you should use play_long_file.py instead.

"""

def percent_dif(lstA,lstB):
    l = []
    ita = 0
    itb = 0
    while (ita < len(lstA)) and (itb < len(lstB)):
        
        if  (lstA[ita] < 0.005) or ( lstB[itb] < 0.005):
            if (lstA[ita] < 0.005):
                ita += 1
            if (lstB[itb] < 0.005):
                itb += 1
        else:
            if lstA[ita] > lstB[itb]:
                l.append(lstB[itb]/lstA[ita])
            else:
                l.append(lstA[ita]/lstB[itb])
            
            ita += 1
            itb += 1
            
    return(l)


def average(lst):
    return(sum(lst)/len(lst))


import argparse


def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text

#parser = argparse.ArgumentParser(description=__doc__)
#parser.add_argument('A1.wav', help='audio file to be played back')
#parser.add_argument('-d', '--device', type=int_or_str,
#                    help='output device (numeric ID or substring)')
#args = parser.parse_args()

try:
    import soundfile as sf
    dataA, fs = sf.read('A1.wav', dtype='float32')
    dataB, fs1 = sf.read('A2.wav', dtype='float32')
    print(average(percent_dif(dataA,dataB)))
    #sd.play(data, fs, device=args.device)
    #status = sd.wait()
    #if status:
    #    parser.exit('Error during playback: ' + str(status))
except KeyboardInterrupt:
    parser.exit('\nInterrupted by user')
except Exception as e:
    print(e)
    parser.exit(type(e).__name__ + ': ' + str(e))






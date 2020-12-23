import datetime
import sounddevice as sd
from scipy.io.wavfile import write

num = 0

def testRecord():
    print("Recording for four second")
    fs = 16000  # Sample rate
    seconds = 4 # Duration of recording
    #Change Range in the line below to record multiple recordings
    for num in range(0, 15):
        print("PRESS RETURN TO RECORD")
        key = input("PRESS RETURN TO RECORD :")
        if key == "":
                myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
                sd.wait()  # Wait until recording is finished
                suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
                name = "./predict/prediction/9/output{}.wav".format(suffix, num)
                write(name, fs, myrecording)
                print("output.wav has been saved to project directory")

testRecord()

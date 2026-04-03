import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(filename="live.wav", duration=5, fs=16000):

    print("\n🎧 Recording system audio...")

    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()

    write(filename, fs, recording)

    return filename
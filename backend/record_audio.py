import pyaudio, wave, os
 
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5

# this module is for quickly creating audio files to test with

audio = pyaudio.PyAudio()

def record_test(out_filename):
    # start recording with default microphone
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    print ("Recording...")
    frames = []
    
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print ("Finished recording.")
    
    print(frames)

    # stop recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
    
    waveFile = wave.open(out_filename, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

record_test(os.path.join("backend", "recordings", "recording-1.wav"))
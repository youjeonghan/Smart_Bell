#-*-coding: utf-8-*-
import pyaudio
import wave
from SoundOutput import sound_output
from decorator import time_chek

@time_chek
def record(save_name):
    """
    input: 저장 파일명
    output: X
    description:
    방문자 안내 음성 출력 후 방문록 녹음
    """
    sound_output("bell_out_of_office")  # 메세지 안내
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100                        # 44100 Hz
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "/home/jeongran/Project/record/"+save_name +".wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

if __name__=="__main__":
    record("test")
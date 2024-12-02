
from pydub import AudioSegment
from pydub.utils import which

# Set ffmpeg path
AudioSegment.converter = which("ffmpeg")
from pydub import AudioSegment
import speech_recognition as sr

# Load the audio file
audio_path = "C:/Users/pshri/Desktop/Coding/output.wav"
audio = AudioSegment.from_file("C:/Users/pshri/Desktop/Coding/output.wav", format="wav")

# Convert to WAV format
wav_path = "converted_audio.wav"
audio.export(wav_path, format="wav")

# Initialize recognizer
recognizer = sr.Recognizer()
with sr.AudioFile(wav_path) as source:
    audio_data = recognizer.record(source)
    transcription = recognizer.recognize_google(audio_data)

print(transcription)

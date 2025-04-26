from gtts import gTTS
import playsound
import os

def speak_vi(text):
    tts = gTTS(text=text, lang='vi')
    tts.save("test.mp3")
    playsound.playsound("test.mp3", True)
    os.remove("test.mp3")

speak_vi("Xin chào. Tôi rất vui được giúp bạn.")

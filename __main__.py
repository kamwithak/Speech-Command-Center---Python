import speech_recognition as sr

class getAudio:
    def __init__(self):
        self.r = sr.Recognizer()
        self.audio = None

    def recordMicorophone(self):
        with sr.Microphone() as source:
            self.audio = self.r.listen(source)
        
    def createAudioFile(self):
        with open("speech.wav", "wb") as f:
            f.write(self.audio.get_wav_data())

    def voiceToText(self):
        with sr.AudioFile("speech.wav") as source:
            self.audio = self.r.record(source)
            print(self.r.recognize_sphinx(self.audio))

if __name__ == "__main__":
    obj = getAudio()
    obj.recordMicorophone()
    obj.createAudioFile()
    obj.voiceToText()


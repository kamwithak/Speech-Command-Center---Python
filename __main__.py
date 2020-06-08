import speech_recognition as sr
from programLauncher import programLauncher

class getAudio:
    def __init__(self):
        self.r = sr.Recognizer()
        self.audio = None
        self.text = ""

    def recordMicorophone(self):
        with sr.Microphone() as source:
            self.audio = self.r.listen(source)
        
    def createAudioFile(self):
        with open("speech.wav", "wb") as f:
            f.write(self.audio.get_wav_data())

    def voiceToText(self):
        try:
            with sr.WavFile("speech.wav") as source:
                self.audio = self.r.record(source)
                self.text = self.r.recognize_google(self.audio, language="en-US")
        except sr.UnknownValueError:
	        print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
	        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        
        return self.text.lower()

if __name__ == "__main__":
    obj = getAudio()
    obj.recordMicorophone()
    obj.createAudioFile()
    print(obj.voiceToText())
    #programLauncher(obj.voiceToText())
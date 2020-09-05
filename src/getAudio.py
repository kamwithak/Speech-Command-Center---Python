import speech_recognition as sr

class getAudio:
    def __init__(self):
        self.r = sr.Recognizer()
        self.audio = None
        self.text = ""

    def recordMicorophone(self):
        print("Accepting input...")
        with sr.Microphone() as source:
            self.audio = self.r.listen(source)
        
    def createAudioFile(self):
        with open("speech.wav", "wb") as f:
            f.write(self.audio.get_wav_data())

    def voiceToText(self):
        try:
            with sr.WavFile("speech.wav") as source:
                self.audio = self.r.record(source)
                self.text = str(self.r.recognize_google(self.audio, language="en-US"))
                if (self.text): print(self.text)
        except sr.UnknownValueError:
	        print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
	        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return self.text.lower()

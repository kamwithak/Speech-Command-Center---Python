import os

class programLauncher:
    def __init__(self, text):
        self.text = text
        self.launch(self.text)
        self.actions = ["launch", "open"]

    def launch(self, text):
        for action in self.actions:
            if (action in text and "chrome" in text):
                os.startfile(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

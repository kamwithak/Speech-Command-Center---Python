import os, winapps

class programLauncher:
    def __init__(self, text):
        self.text = text
        self.actionLabels = ["launch", "start", "open", "begin", "kick off", "commence", "turn on", "give me", "instantiate", "initialize"]
        self.programLables = self.populateProgramLabels()
        # ~
        #self.launch(self.text)

    def populateProgramLabels(self):
        return [i.name for i in self.findAllLocalPrograms()]
        
    def findAllLocalPrograms(self):
        return [app for app in winapps.list_installed()]
        
    def launch(self, text):
        for action in self.actionLabels:
            for program in self.programLabels:
                if (action in text and program in text):
                    os.startfile(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
                    return 

i = programLauncher("launch chrome")
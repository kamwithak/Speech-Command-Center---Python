import os, winapps

class programLauncher:
    def __init__(self, text):
        self.text = text
        self.actionLabels = [
            "launch",
            "start",
            "open",
            "begin",
            "kick off",
            "commence",
            "turn on",
            "give me",
            "instantiate",
            "initialize"
        ]
        self.programDict = self.getInstalledPrograms()
        # ~~~~~~~~~~~~~~~~~~~~~
        print(self.programDict)
        # ~~~~~~~~~~~~~~~~~~~~~
        self.launch(self.text)

    '''
    @args: None
    @return: dictionary where keys are the program names and values are the program locations
    '''
    def getInstalledPrograms(self):
        programDict = {}
        for localProgram in winapps.list_installed():
            programDict[localProgram.name] = localProgram.install_location
        return programDict
    
    '''
    @args: str
    @return: binary decision regarding successful launch of specified program
    '''
    def launch(self, text):
        for action in self.actionLabels:
            for program in self.programDict:
                if (action in text and program in text):
                    os.startfile(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
                    return 

i = programLauncher("launch chrome")

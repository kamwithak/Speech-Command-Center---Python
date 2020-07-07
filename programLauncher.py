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
        self.programDict = self.getLocalProgramData()
        # ~~~~~~~~~~~~~~~~~~~~~
        #print(self.programDict)
        # ~~~~~~~~~~~~~~~~~~~~~
        self.start(self.text)

    '''
    @args: None
    @description: gets needed locally installed software metadata
    @return: dict where keys == name and values == [install_dir, name_of_program]
    '''
    def getLocalProgramData(self):
        programDict = {}
        for localProgram in winapps.list_installed():
            programDict[localProgram.name] = [
                localProgram.install_location,              # 0th index
                localProgram.name.lower().split()           # 1st index
                ]
        return programDict
    
    '''
    @args: str, str
    @description: execution of .exe in programLocation directory
    @return: binary decision pertaining to the succesfull launch of programName
    '''
    def launch(self, programLocation, programName):
        #os.startfile()
        print(programName)
        print(programLocation)
        pass

    '''
    @args: str
    @description: acceptance criteria for successful launch 
    @return: None
    '''
    def start(self, text):
        for action in self.actionLabels:
            for bucket in self.programDict:
                for ball in self.programDict[bucket][1]:
                    if (action in text and ball in text):
                        self.launch(self.programDict[bucket][0], self.programDict[bucket][1])
                        return 

i = programLauncher("launch sublime")

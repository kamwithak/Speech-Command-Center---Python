import os
import winapps
import glob

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
        # for program in self.programDict:
        #     print(str(program) + "     -     " + str(self.programDict[program][0]))
        # ~~~~~~~~~~~~~~~~~~~~~
        
        self.startEngine(self.text)

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
    @description: execution of .exe in programDirectory
    @return: binary decision pertaining to the succesfull launch of programName
    '''
    def launch(self, programLocation, programName):
        executablePaths = []
        for executablePath in glob.iglob(str(programLocation) + "\*.exe", recursive=True):
            executablePaths.append(str(executablePath))
        # ~~~~~~~~~~~~~
        if not executablePaths:
            print(f'Installations missing - executablePaths: {executablePaths}')
        for i in range(len(executablePaths)):
            print(str(i+1) + ") " + str(executablePaths[i]))
        # ~~~~~~~~~~~~~
        j = int(input("Which to launch? "))
        if (j > 0 and j <= len(executablePaths)):
            print(f'Launching {executablePaths[j-1]}')
            os.startfile(executablePaths[j-1])
            return True
        return False

    '''
    @args: str
    @description: acceptance criteria for successful launch 
    @return: None
    '''
    def startEngine(self, text):
        for action in self.actionLabels:
            for bucket in self.programDict:
                for ball in self.programDict[bucket][1]:
                    if (action in text and ball in text):
                        self.launch(self.programDict[bucket][0], self.programDict[bucket][1])
                        return 
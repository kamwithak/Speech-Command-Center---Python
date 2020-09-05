from src.programLauncher import programLauncher
from src.getAudio import getAudio

if __name__ == "__main__":
    audioDriver = getAudio()
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    audioDriver.recordMicorophone()
    audioDriver.createAudioFile()
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    programLauncher(audioDriver.voiceToText())
    
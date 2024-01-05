import os

def speak(text:str)->None:
    """
    This function is responsible 
    for taking text as input 
    and gives audio as output file.
    """
    voice="en-US-AriaNeural"

    command=f'edge-tts --voice "{voice}" --text "{text}" --write-media "output.mp3"'

    os.system(command)

speak("Hello I am Sai Raghava working in software Industry.")
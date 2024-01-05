import os
import pygame

def speak(text:str)->None:
    """
    This function is responsible 
    for taking text as input 
    and gives audio as output file.
    """
    voice="en-US-AriaNeural"

    command=f'edge-tts --voice "{voice}" --text "{text}" --write-media "output.mp3"'

    os.system(command)

    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)
    finally:
        pygame.mixer.stop()
        pygame.mixer.quit()


speak("Hello I am Sai Raghava working in software Industry.")
import pyttsx3


def speak(text):

    print("Starting TTS")

    engine = pyttsx3.init()

    engine.say(text)

    engine.runAndWait()

    engine.stop()

    print("Finished TTS")
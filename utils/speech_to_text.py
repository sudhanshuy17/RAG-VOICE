import speech_recognition as sr


# Initialize recognizer and microphone once
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Adjust for ambient noise once at startup (quick, ~1 second)
with microphone as source:
    recognizer.adjust_for_ambient_noise(source, duration=1)


def listen():
    """
    Records audio from the microphone and converts it to text
    using Google Speech Recognition.
    Automatically stops when the user stops talking.
    """

    print("\n Listening...")

    with microphone as source:
        try:
            audio = recognizer.listen(
                source,
                timeout=5,           # Max wait for speech to start
                phrase_time_limit=10  # Max duration of a single phrase
            )
        except sr.WaitTimeoutError:
            print("\n [STT] No speech detected.")
            return ""

    try:
        text = recognizer.recognize_google(audio, language="en-US")
        print(f"\n You Said: {text}")
        return text.strip()

    except sr.UnknownValueError:
        print("\n [STT] Could not understand audio.")
        return ""

    except sr.RequestError as e:
        print(f"\n [STT] Google API error: {e}")
        return ""

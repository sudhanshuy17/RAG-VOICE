import speech_recognition as sr


def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("\nI'm Listening...")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        audio = recognizer.listen(source)

    try:

        query = recognizer.recognize_google(audio)

        print(f"\n You Said: {query}")

        return query

    except sr.UnknownValueError:

        print("Could not understand audio")

        return None

    except Exception as e:

        print(e)

        return None
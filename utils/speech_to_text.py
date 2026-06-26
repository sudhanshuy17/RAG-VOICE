import speech_recognition as sr
import io
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Initialize once
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Groq Whisper client (singleton)
_groq_client = Groq(api_key=os.getenv("WHISPHER_V3_API_KEY"))

# Calibrate once
with microphone as source:
    recognizer.adjust_for_ambient_noise(source, duration=1)


def _recognize(audio):
    """
    Converts recorded audio to text using Groq whisper-large-v3-turbo.
    """

    try:
        # Convert SpeechRecognition audio to WAV bytes
        wav_data = audio.get_wav_data()

        # Send to Groq Whisper API
        transcription = _groq_client.audio.transcriptions.create(
            model="whisper-large-v3-turbo",
            file=("audio.wav", io.BytesIO(wav_data)),
            language="en",
        )

        text = transcription.text.strip()
        return text

    except Exception as e:
        print(f"\n[STT] Groq Whisper Error: {e}")
        return ""


def listen():
    """
    Normal listening mode.
    Waits until the user speaks.
    """

    print("\nListening...")

    with microphone as source:

        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )

        except sr.WaitTimeoutError:

            print("\n[STT] No speech detected.")

            return ""

    text = _recognize(audio)

    if text:
        print(f"\nYou Said: {text}")

    return text


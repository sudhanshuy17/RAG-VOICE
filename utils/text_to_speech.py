# pyttsx3 removed instead of that we are using edge_tts

import asyncio
import edge_tts
import pygame
import tempfile
import os
import time

# VOICE = "en-US-ChristopherNeural"
#VOICE = "en-US-BrianNeural"    # sounds well
VOICE = "en-US-RogerNeural"

async def _generate_audio(text, filename):
    # adjusted speaking rate so it could sound like a financial mentor
    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE,
        rate="-5%",
        pitch="-2Hz"
    )

    await communicate.save(filename)

def speak(text):
    with  tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp3"
    ) as temp:
        filename = temp.name

    try:
        # Use a new event loop each time to avoid Windows
        # ProactorEventLoop issues with repeated asyncio.run() calls
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(
                _generate_audio(text, filename)
            )
        finally:
            loop.close()

        if not os.path.exists(filename) or os.path.getsize(filename) == 0:
            print(" [TTS] Error: Audio file was not generated.")
            return

        if not pygame.mixer.get_init():
            pygame.mixer.init()

        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        # Small delay to let pygame start playback before checking get_busy()
        time.sleep(0.3)

        clock = pygame.time.Clock()
        while pygame.mixer.music.get_busy():
            clock.tick(10)
        
        pygame.mixer.music.unload()

    except Exception as e:
        print(f" [TTS] Error during speech: {e}")

    finally:
        try:
            if os.path.exists(filename):
                os.remove(filename)
        except Exception:
            pass

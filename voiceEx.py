import asyncio
import edge_tts

async def speak():
    communicate = edge_tts.Communicate(
        text="Hello, welcome to my Voice RAG project!",
        voice="en-US-ChristopherNeural"
    )

    await communicate.save("response.mp3")

asyncio.run(speak())
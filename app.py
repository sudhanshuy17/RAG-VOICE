from utils.retriever import get_retriever
from utils.llm import get_llm
from utils.speech_to_text import listen
from utils.text_to_speech import speak
from utils.text_formatter import format_for_speech

print("\n Initializing Voice RAG...\n")

retriever = get_retriever()
llm = get_llm()

print("Voice RAG Ready")
print("Say 'exit', 'quit', or 'stop' to end the conversation.\n")

SYSTEM_PROMPT = """
You are Robert Kiyosaki, bestselling author of Rich Dad Poor Dad and Cashflow Quadrant.

Your personality:
- Calm, confident and encouraging.
- Speak like you're mentoring someone one-on-one.
- Sound like a podcast host or keynote speaker.
- Never sound robotic.
- Never introduce yourself unless the user explicitly asks who you are.

Response Guidelines:

1. Use the retrieved context as your primary source.

2. If the answer is not completely available in the context,
you may answer using your broader teachings about:
- Financial Literacy
- Entrepreneurship
- Investing
- Cashflow
- Assets vs Liabilities

When doing so, briefly say:

"This comes from my broader teachings, not directly from Cashflow Quadrant."

3. Write for SPEAKING, not reading.

That means:
- Short sentences.
- Natural pauses.
- Conversational language.
- Avoid large paragraphs.
- Avoid unnecessary lists.
- Explain ideas like you're talking to one person.

4. Never make up facts from the document.

5. Keep answers between 80 and 180 words unless the user asks for more detail.

6. End with one practical takeaway whenever appropriate.

Context:
{context}

User Question:
{query}
"""

while True:

    query = listen()

    if not query:
        continue

    if query.lower() in ["exit", "quit", "stop"]:

        goodbye = (
            "Goodbye. Remember, financial freedom isn't about earning more money. "
            "It's about building assets that work for you. Keep learning, keep investing, and I'll see you next time."
        )

        print("\nGoodbye\n")
        print(goodbye)

        speak(goodbye)

        break

    try:

        docs = retriever.invoke(query)

        context = "\n\n".join(
            doc.page_content for doc in docs
        )

        prompt = SYSTEM_PROMPT.format(
            context=context,
            query=query
        )

        response = llm.invoke(prompt)

        answer = response.content.strip()

        print("\nAnswer:\n")
        print(answer)

        speech = format_for_speech(answer)

        speak(speech)

    except Exception as e:

        print(f"\nError: {e}")

        speak("I'm sorry. I encountered an unexpected error while answering your question.")
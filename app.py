from utils.retriever import get_retriever
from utils.llm import get_llm
from utils.speech_to_text import listen
from utils.text_to_speech import speak

print("\n Initializing Voice RAG...\n")

retriever = get_retriever()
llm = get_llm()

print("Voice RAG Ready")
print("Say 'exit', 'quit', or 'stop' to end the conversation.\n")

while True:

    query = listen()

    if not query:
        continue

    if query.lower() in ["exit", "quit", "stop"]:

        goodbye_message = (
            "Goodbye. Remember, financial freedom is not about how much money you make, "
            "but how much money works for you."
        )

        print("\nAnswer:\n")
        print(goodbye_message)

        speak(goodbye_message)

        break

    docs = retriever.invoke(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are Robert Kiyosaki, the bestselling author of "Rich Dad Poor Dad"
and "Cashflow Quadrant".

You speak with confidence, wisdom, and a conversational tone,
just like in your books, interviews, and seminars.

Rules:

1. NEVER start your response with an introduction or "Hello, I'm Robert Kiyosaki..."
   unless the user EXPLICITLY asks "who are you?" or "introduce yourself."
   Just answer the question directly.

2. If the answer exists in the provided context,
use the context as the primary source of truth. Answer in your own words.

3. If the context does not contain the answer,
you may answer using your broader teachings about:
   - Financial Literacy
   - Entrepreneurship
   - Investing
   - Cashflow
   - Assets vs Liabilities
   But briefly note: "This is from my broader teachings, not directly from Cashflow Quadrant."

4. Keep answers:
   - Practical
   - Motivational
   - Easy to understand
   - Under 250 words

Context from Cashflow Quadrant:

{context}

Question:

{query}
"""

    try:

        response = llm.invoke(prompt)

        answer = response.content

        print("\n Answer:\n")
        print(answer)

        speak(answer)

    except Exception as e:

        error_message = f"An error occurred: {str(e)}"

        print(error_message)

        speak("Sorry, I encountered an error while processing your question.")
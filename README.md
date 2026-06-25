# 🎙️ Voice RAG Chatbot

A **Voice-enabled Retrieval-Augmented Generation (RAG)** chatbot built with **Python**, **LangChain**, **ChromaDB**, and **Groq LLM**. The application allows users to ask questions through their microphone, retrieves relevant information from a PDF knowledge base, generates intelligent responses using an LLM, and replies back with synthesized speech.

---

## 🚀 Features

* 🎤 Voice Input using Speech Recognition
* 📄 PDF Knowledge Base
* 🔍 OCR-based PDF Text Extraction (PyMuPDF + Tesseract)
* ✂️ Intelligent Text Chunking
* 🧠 Semantic Search using ChromaDB
* 🤖 Groq Llama 3 Integration
* 🔊 Text-to-Speech Responses
* 💬 Interactive Voice Conversation
* 📦 Modular Python Architecture
* 🖥️ Ready to Package as a Windows Executable

---

## 🏗️ System Architecture

```text
                 User
                   │
                   ▼
          Speech To Text (STT)
        (SpeechRecognition)
                   │
                   ▼
              User Query
                   │
                   ▼
        ChromaDB Semantic Search
                   │
                   ▼
          Relevant PDF Chunks
                   │
                   ▼
           Groq Llama 3 (LLM)
                   │
                   ▼
          Generated Response
                   │
                   ▼
        Text To Speech (TTS)
             (edge_tts)
                   │
                   ▼
              Voice Output
```

---

## 📁 Project Structure

```text
voice-rag/
│
├── app.py
├── requirements.txt
├── .env
│
├── data/
│   └── cashflow_book.pdf
│
├── db/
│   └── chroma_db/
│
└── utils/
    ├── __init__.py
    ├── ocr_loader.py
    ├── vector_store.py
    ├── retriever.py
    ├── llm.py
    ├── speech_to_text.py
    └── text_to_speech.py
```

---

## 🛠️ Technologies Used

| Category           | Technology                             |
| ------------------ | -------------------------------------- |
| Language           | Python                                 |
| LLM                | Groq (Llama 3)                         |
| Framework          | LangChain                              |
| Vector Database    | ChromaDB                               |
| Embeddings         | sentence-transformers/all-MiniLM-L6-v2 |
| OCR                | PyMuPDF + Tesseract OCR                |
| Speech Recognition | SpeechRecognition                      |
| Text To Speech     | edge_tts                               |
| Environment        | python-dotenv                          |

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/voice-rag.git
cd voice-rag
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

---

## 📚 Prepare the Knowledge Base

Place your PDF inside:

```text
data/
```

Example:

```text
data/
└── cashflow_book.pdf
```

Run the vector store creation script to generate embeddings and build the Chroma database.

---

## ▶️ Run the Application

```bash
python app.py
```

---

## 💬 Example Conversation

**User**

> What is the Cashflow Quadrant?

**Assistant**

> The Cashflow Quadrant categorizes people based on how they earn income. The four quadrants are Employee (E), Self-Employed (S), Business Owner (B), and Investor (I).

---

## 📌 Workflow

1. User speaks through the microphone.
2. Speech is converted into text.
3. The query is embedded and searched in ChromaDB.
4. The most relevant document chunks are retrieved.
5. Groq Llama 3 generates a context-aware answer.
6. The response is converted into speech.
7. The assistant speaks the answer back to the user.

---

## 📈 Future Enhancements

* Multi-PDF Support
* Conversation Memory
* Streaming Responses
* Speaker Identification
* Faster-Whisper Integration
* Edge-TTS for Natural Voice
* GUI/Desktop Application
* Executable (.exe) Packaging

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Sudhanshu Yadav**

* Full Stack Developer
* AI & LLM Enthusiast
* MERN Stack Developer
* Backend Engineer

If you found this project useful, consider giving it a ⭐ on GitHub.

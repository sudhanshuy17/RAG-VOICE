Voice RAG inspiered from the book Cashflow® Quadrant by Robert Kiosaki

The pipeline (Ingestion Pipeline) : ocr_loader.py (Loads the pdf and extract the data using tessaract) -> vector_store.py (creates chunks from the extracted data using RecursiveCharacterTextSplitter, and also creating embeddings using sentence-transformers/all-MiniLM-L6-v2 and store them in the vector_db ie,. chroma_db)


(Retrieval Pipeline): retriever.py (retriveing data from the vector_db using size 3 chunks, search_kwargs={"k": 3}) -> llm.py (model intialized using temperature = 0.2) -> [seperate util functions (speech_to_text and text_to_speech)-> for building the voice model] -> app.py (has the infinite while loop that runs the model based on the system prompt we have provided and the knowledge base coming from the retriever.py, using voice model functions reading responses and taking the user prompt from the mic input)

To stop the conversation with the model you have to say ('exit', 'quit', or 'stop')

All the required libraries are listed in the requirements.txt -> pip install -r requirements.txt



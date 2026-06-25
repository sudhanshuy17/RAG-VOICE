import os
import pymupdf
from langchain_core.documents import Document


def extract_text_from_pdf(pdf_filename="cashflow.pdf"):
    """
    Extract text from a PDF using PyMuPDF OCR and
    return a list of LangChain Documents.
    """

    pdf_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..",
        "data",
        pdf_filename
    )

    tessdata_path = r"C:\Program Files\Tesseract-OCR\tessdata"

    doc = pymupdf.open(pdf_path)

    documents = []

    print(f"Loading PDF: {pdf_filename}")

    for page_num, page in enumerate(doc):

        text_page = page.get_textpage_ocr(
            language="eng",
            tessdata=tessdata_path,
            full=True
        )

        text = page.get_text(
            "text",
            textpage=text_page
        )

        documents.append(
            Document(
                page_content=text,
                metadata={
                    "source": pdf_filename,
                    "page": page_num + 1
                }
            )
        )

        print(f"Processed Page {page_num + 1}")

    print(f"\nTotal pages loaded: {len(documents)}")

    return documents
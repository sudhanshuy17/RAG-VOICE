import re


FINANCIAL_TERMS = {
    "AI": "A I",
    "LLM": "L L M",
    "API": "A P I",
    "RAG": "R A G",
    "OCR": "O C R",
    "CPU": "C P U",
    "GPU": "G P U",
    "PDF": "P D F",
    "ROI": "R O I",
    "CEO": "C E O",
    "CTO": "C T O",
}


def format_for_speech(text: str) -> str:
    """
    Formats LLM output so it sounds more natural when spoken by Edge-TTS.
    """

    if not text:
        return ""

    # Remove markdown formatting
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\*(.*?)\*", r"\1", text)
    text = re.sub(r"`(.*?)`", r"\1", text)
    text = re.sub(r"#+\s*", "", text)

    # Expand abbreviations
    for word, replacement in FINANCIAL_TERMS.items():
        text = re.sub(rf"\b{word}\b", replacement, text)

    # Expand symbols
    text = text.replace("&", " and ")
    text = text.replace("%", " percent")
    text = text.replace("$", " dollars ")

    # Better speaking pauses
    text = text.replace(":", ".")
    text = text.replace(";", ".")
    text = text.replace("(", ", ")
    text = text.replace(")", "")

    # Give numbered lists breathing room
    text = re.sub(r"(\d+)\.", r"\n\1.", text)

    # Pause after commas
    text = text.replace(",", ", ")

    # Separate consecutive periods
    text = re.sub(r"\.\s*", ". ", text)

    # Collapse extra whitespace
    text = re.sub(r"\s+", " ", text)

    return text.strip()
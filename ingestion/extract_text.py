from pathlib import Path
from pypdf import PdfReader


PDF_PATH = Path("data/raw_docs/django-readthedocs-io-en-6.0.x.pdf")
OUTPUT_PATH = Path("data/extracted_docs/django-readthedocs-io-en-6.0.x.txt")

def extract_pdf_text(pdf_path: Path) -> str:
    reader = PdfReader(str(pdf_path))
    pages_text = []
    for page_num,page in enumerate(reader.pages):
        print("processing page:", page_num)
        text = page.extract_text()
        if text:
            pages_text.append(text)
        else:
            print(f"Warning: No text found on page {page_num}")

    return "\n".join(pages_text)


def main():
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"PDF not found at {PDF_PATH}")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    text = extract_pdf_text(PDF_PATH)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Extracted text saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
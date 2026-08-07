from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)
POPPLER_PATH = (
    r"C:\Users\RAJEEV SHUKLA\Downloads\Release-26.02.0-0\poppler-26.02.0\Library\bin"
)


# ======================================
# Extract Text From PDF
# ======================================


def extract_text(pdf_path):

    print("Opening PDF:", pdf_path)

    reader = PdfReader(pdf_path)

    print("Pages:", len(reader.pages))

    text = ""

    for i, page in enumerate(reader.pages):

        extracted = page.extract_text()

        print(f"Page {i+1} Extracted Length:", len(extracted) if extracted else 0)

        if extracted:
            text += extracted + "\n"

    print("Total Extracted:", len(text))

    return text
# ======================================
# OCR Extraction
# ======================================

def extract_text_using_ocr(pdf_path):

    print("\nRunning OCR on:", pdf_path)

    images = convert_from_path(
        pdf_path,
        poppler_path=POPPLER_PATH
    )

    text = ""

    for i, image in enumerate(images):

        print(f"OCR Page {i+1}")

        extracted = pytesseract.image_to_string(image)

        text += extracted + "\n"

    print("OCR Extracted Characters:", len(text))

    return text

def extract_all_pdfs(folder_path):

    text = ""

    print("Folder:", folder_path)
    print("Files:", os.listdir(folder_path))

    for file in os.listdir(folder_path):

        print("Checking:", file)

        if file.lower().endswith(".pdf"):

            pdf_path = os.path.join(folder_path, file)

            print("Reading:", pdf_path)
            print("Size:", os.path.getsize(pdf_path))

            extracted = extract_text(pdf_path)

            print("Extracted characters:", len(extracted))

            # If very little text was extracted, use OCR
            if len(extracted.strip()) < 300:

                print("Very little text found. Switching to OCR...")

                extracted = extract_text_using_ocr(pdf_path)

            print("Extracted characters:", len(extracted))

            text += extracted
            text += "\n"

    print("Final Text Length:", len(text))

    return text
# ======================================
# Split Text Into Chunks
# ======================================

def chunk_text(text):

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=1000,

        chunk_overlap=200,

        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]

    )

    chunks = splitter.split_text(text)

    return chunks


# ======================================
# Retrieve Relevant Chunks
# ======================================

def retrieve_chunks(vector_db, question):

    docs = vector_db.similarity_search(

        question,

        k=5

    )

    context = ""

    sources = []

    for doc in docs:
        print("Metadata:", doc.metadata)

        context += doc.page_content

        context += "\n\n"

        sources.append(doc.metadata)

    return context, sources
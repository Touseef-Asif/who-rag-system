from loaders.pdf_loader import load_pdf

from config.settings import settings


docs = load_pdf(settings.PDF_PATH)

print(f"\nTotal Pages: {len(docs)}\n")

print(docs[0].page_content[:1000])

print("\nMetadata:\n")

print(docs[0].metadata)
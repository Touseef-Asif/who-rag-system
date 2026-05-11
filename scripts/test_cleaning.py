from loaders.pdf_loader import load_pdf

from preprocess.text_cleaner import clean_documents

from config.settings import settings


docs = load_pdf(settings.PDF_PATH)

cleaned_docs = clean_documents(docs)

print(cleaned_docs[0].page_content[:1000])
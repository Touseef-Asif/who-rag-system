from loaders.pdf_loader import PDFLoader

PDF_PATH = "data/raw/who_substances_surveillance.pdf"

pdf_loader = PDFLoader(PDF_PATH)

docs = pdf_loader.load()

print("\n Total pages loaded:", len(docs))

print("\n Sample text:\n")
print(docs[0]["text"][:500])

print("\n Metadata:\n")
print(docs[0]["metadata"])
import os

from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

pdf_folder = 'resources'
pdf_files = [file for file in os.listdir(pdf_folder) if file.endswith('.pdf')]
print(pdf_files)
cnt = 0
for item in pdf_files:
    # fp = open(item, "rb")
    fp = open('./resources/' + item, 'rb')
    cnt += 1
    print(f"第{cnt}篇论文")
    resource = PDFResourceManager()
    laparam = LAParams()
    device = PDFPageAggregator(resource, laparams=laparam)
    interpreter = PDFPageInterpreter(resource, device)
    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        layout = device.get_result()
        for out in layout:
            if hasattr(out, "get_text"):
                print(out.get_text())

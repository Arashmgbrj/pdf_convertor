from pdf2docx import Converter
def test1():
  pdf_file = 'send2.pdf'
  docx_file = 'test.docx'
  # convert pdf to docx
  cv = Converter(pdf_file)
  cv.convert(docx_file)      # all pages by default
  cv.close()
test1()
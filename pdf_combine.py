import PyPDF2
import sys

inputs = sys.argv[1:]  # Includes as many arguments as are passed


def merge_pdfs(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('super.pdf')
    merger.close()


merge_pdfs(inputs)

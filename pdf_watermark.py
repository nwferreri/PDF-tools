# Adds a watermark to all pages in a PDF

# Import tools
from pypdf import PdfWriter, PdfReader


# Get watermark from user
while True:
    try:
        wm_file = input("Enter watermark PDF filename: ")
        watermark = PdfReader(wm_file).pages[0]
    except FileNotFoundError:
        print("ERROR: File does not exist.")
    else:
        break

# Get document to be watermarked from user
while True:
    try:
        doc = input("Enter PDF filename: ")
        writer = PdfWriter(clone_from=doc)
    except FileNotFoundError:
        print("ERROR: File does not exist.")
    else:
        break

# Add watermark to all pages
for page in writer.pages:
    page.merge_page(watermark, over=False)

# Get output filepath and write it
out_file = input("Enter output PDF filename: ")
if out_file[-4:] != '.pdf':
    out_file = out_file + '.pdf'
writer.write(out_file)
print("All done!")

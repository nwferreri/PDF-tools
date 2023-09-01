# Combines PDFs given by the user into one document

# Import tools
from pypdf import PdfWriter


# Open PDF writer
merger = PdfWriter()

# Parse user input into list of files and append them
while True:
    try:
        user_input = input("Enter files to merge, separated by commas: ")
        pdf_list = user_input.split(',')
        for pdf in pdf_list:
            merger.append(pdf)
    except FileNotFoundError:
        print("One or more files not found. Please try again.\n"
            "TIP: Separate files by commas only, no spaces.")
    else:
        break 

# Get output filepath and write it
out_file = input("Enter output PDF filename: ")
if out_file[-4:] != '.pdf':
    out_file = out_file + '.pdf'
merger.write(out_file)
merger.close()
print("All done!")

# Rotates a page in a given pdf by specified amount.

# Import tools
from pypdf import PdfWriter, PdfReader


# Get input file from user
while True:
    try:
        file = input("Enter PDF filepath/name: ")
        reader = PdfReader(file)
    except FileNotFoundError:
        print("ERROR: File does not exist.")
    else:
        break

# Open writer as clone of document
writer = PdfWriter(clone_from=file)

# Get page number to rotate
while True:
    try:
        index = int(input("Page number to rotate: ")) - 1
        if index >= 0:  # Don't allow negative indexing
            writer.pages[index]
        else:
            print("ERROR: Not a valid page number.")
            continue
    except ValueError:
        print("ERROR: Please enter an integer.")
    except IndexError:
        print("ERROR: Not a valid page number.")
    else:
        break

# Get rotation and rotate selected page
while True:
    try:
        rotation = int(input("Rotate clockwise by? (mulitple of 90): "))
        writer.pages[index].rotate(rotation)
    except ValueError:
        print("ERROR: Please enter a number that is a multiple of 90.")
    else:
        break

# Get output filepath and write it
out_file = input("Enter output PDF filepath/name: ")
if out_file[-4:] != '.pdf':
    out_file = out_file + '.pdf'
with open(out_file, "wb") as fp:
    writer.write(fp)
print("All done!")

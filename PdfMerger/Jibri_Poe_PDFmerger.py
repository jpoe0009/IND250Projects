import sys
import os
from PyPDF2 import PdfMerger, PdfReader


def main():

    # -----------------------------
    # 1 & 2. Read command line args
    # -----------------------------
    if len(sys.argv) < 2:
        print("Error: Merge file name not specified.")
        print("Usage: python pdfmerger.py filename [-t]")
        sys.exit(1)

    output_name = sys.argv[1] + ".pdf"
    extract_text = False

    # Bonus option check
    if len(sys.argv) > 2 and sys.argv[2] == "-t":
        extract_text = True

    # -----------------------------
    # 3. Initialize merger object
    # -----------------------------
    merger = PdfMerger()

    # -----------------------------
    # 4. Retrieve files
    # -----------------------------
    files = os.listdir(".")

    # -----------------------------
    # 5. Filter pdf files
    # -----------------------------
    pdf_files = [f for f in files if f.lower().endswith(".pdf")]

    # -----------------------------
    # 6. Sort alphabetically
    # -----------------------------
    pdf_files.sort()

    # Remove output file if present
    pdf_files = [f for f in pdf_files if f != output_name]

    # -----------------------------
    # 7. Report files found
    # -----------------------------
    print("PDF files found:", len(pdf_files))
    print("List:")

    for file in pdf_files:
        print(file)

    if len(pdf_files) == 0:
        print("No PDF files found.")
        sys.exit()

    # -----------------------------
    # 8. Prompt user
    # -----------------------------
    choice = input("Continue (y/n): ")

    if choice.lower() != "y":
        print("Operation cancelled.")
        sys.exit()

    # -----------------------------
    # 9. Append PDFs
    # -----------------------------
    for pdf in pdf_files:
        print("Adding:", pdf)
        merger.append(pdf)

    # -----------------------------
    # 10. Export merged PDF
    # -----------------------------
    merger.write(output_name)
    merger.close()

    print("Merged PDF saved as:", output_name)

    # -----------------------------
    # Bonus: Extract text
    # -----------------------------
    if extract_text:

        print("Extracting text from merged PDF...")

        reader = PdfReader(output_name)
        text = ""

        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text()

        text_file = sys.argv[1] + ".txt"

        with open(text_file, "w", encoding="utf-8") as f:
            f.write(text)

        print("Text saved to:", text_file)


# Run program
if __name__ == "__main__":
    main()

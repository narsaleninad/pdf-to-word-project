from pdf_reader import extract_lines
from word_builder import build_word

PDF_PATH = "django_assignment.pdf"
OUTPUT_DOC = "django_word.docx"

lines = extract_lines(PDF_PATH)
build_word(lines, OUTPUT_DOC)

print("PDF converted to Word successfully!")

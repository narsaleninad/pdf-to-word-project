import pdfplumber

def extract_lines(pdf_path):
    lines = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                for line in text.split("\n"):
                    lines.append(line.strip())
            lines.append("__PAGE_BREAK__")

    return lines

import PyPDF2
from docx import Document


def pdf_to_docx(input_pdf_path, output_docx_path):
    pdf_reader = PyPDF2.PdfReader(input_pdf_path)
    doc = Document()

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        doc.add_paragraph(text)

    doc.save(output_docx_path)
    print(f"PDF successfully converted to {output_docx_path}")


input_pdf_path = "/Users/houhjim/Downloads/HarveyYao_Resume_NV.pdf"
output_docx_path = "/Users/houhjim/Downloads/HarveyYao_Resume_NV.docx"
pdf_to_docx(input_pdf_path, output_docx_path)
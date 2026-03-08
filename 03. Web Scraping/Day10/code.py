"""
Read PDF files using PyMuPDF library

"""

import fitz

def read_pdf(file_path):
    doc = fitz.open(file_path)
    all_text = ""
    
    for page_num in range(len(doc)):
        page = doc[page_num]  
        all_text += page.get_text()  
    
    doc.close()
    return all_text

if __name__ == "__main__":
    file_path = "sample.pdf"
    try:
        text = read_pdf(file_path)
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(text)

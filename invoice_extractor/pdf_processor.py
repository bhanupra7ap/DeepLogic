
import pytesseract
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
from pdf2image import convert_from_path
import os

def extract_text_from_file(file_path):
    
    if file_path.lower().endswith('.pdf'):
        try:
            return extract_text_from_pdf(file_path)
        except (PDFInfoNotInstalledError, PDFPageCountError, PDFSyntaxError):
            # Handle PDF processing errors
            return "Error: Unable to process PDF file"
    elif file_path.lower().endswith(('.jpg', '.jpeg', '.png')):
        return extract_text_from_image(file_path)
    else:
        return "Error: Unsupported file format"

def extract_text_from_pdf(pdf_path):
    
    pages = convert_from_path(pdf_path)
    text = ''
    for page in pages:
        text += pytesseract.image_to_string(page)
    return text

def extract_text_from_image(image_path):
    
    return pytesseract.image_to_string(image_path)


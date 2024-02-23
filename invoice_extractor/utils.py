
import os
from .pdf_processor import extract_text_from_pdf, extract_key_value_pairs

def extract_data_from_pdf(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    key_value_pairs = extract_key_value_pairs(text)
    os.remove(pdf_path)
    return key_value_pairs


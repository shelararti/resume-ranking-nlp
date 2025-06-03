import os
import pdfplumber
import spacy

nlp = spacy.load("en_core_web_sm")

def preprocess(text):
    doc = nlp(text.lower())
    return " ".join([token.lemma_ for token in doc if token.is_alpha and not token.is_stop])

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return text.strip()

def load_and_preprocess_resumes(resume_folder):
    if not os.path.exists(resume_folder):
        raise FileNotFoundError(f"Folder '{resume_folder}' not found!")
    
    resumes = {}
    for filename in os.listdir(resume_folder):
        if filename.endswith(".pdf"):
            file_path = os.path.join(resume_folder, filename)
            raw_text = extract_text_from_pdf(file_path)
            if raw_text:
                resumes[filename] = preprocess(raw_text)
    if not resumes:
        raise ValueError("No resumes found or extracted in the folder!")
    return resumes

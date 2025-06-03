from resume_processing import load_and_preprocess_resumes
from ranking_reporting import rank_resumes

job_title = "Data Analyst"
job_description = """
Resume Ranking System using NLP and TF-IDF

This Python script ranks resumes based on their relevance to a given job description using natural language processing techniques.

🔧 Features:
- Extracts text from multiple PDF resumes using `pdfplumber`.
- Uses spaCy to preprocess and lemmatize text (removing stopwords, punctuation, etc.).
- Converts both the job description and all resumes into TF-IDF vectors.
- Calculates cosine similarity between the job description and each resume.
- Outputs a ranked list of resumes based on similarity scores.
- Saves the ranking results to a CSV file.
- Displays the top terms from the best-matching resume.

📁 Folder Requirement:
- Place all PDF resumes in a folder named `resumes` within the current working directory.

🧠 Libraries Used:
- `pdfplumber` for PDF text extraction
- `spacy` for NLP preprocessing
- `scikit-learn` for TF-IDF vectorization and similarity scoring
- `csv`, `os`, and `datetime` for file handling

💼 Use Case:
Useful for HR teams, recruiters, or developers building AI-based applicant tracking systems (ATS) to filter the most relevant candidates automatically.

"""


resume_folder = "./resumes"

try:
    resumes = load_and_preprocess_resumes(resume_folder)
    ranked_resumes = rank_resumes(job_description, resumes, job_title)
except Exception as e:
    print(f"Error: {e}")

# 📊 Resume Ranking System using NLP

This Python-based project ranks PDF resumes based on their relevance to a specific job description using **Natural Language Processing (NLP)** techniques. It's designed for HR teams, recruiters, or developers looking to build AI-powered applicant tracking tools.

---

## 🚀 Features

- 📄 Extracts text from multiple PDF resumes using `pdfplumber`
- 🧠 Uses `spaCy` for text preprocessing (lemmatization, stopword removal, etc.)
- 📈 Converts documents into TF-IDF vectors and compares using cosine similarity
- 📋 Outputs a ranked list of resumes and saves it to a CSV file
- 🏅 Displays top terms from the best-matching resume

---

## 📁 Folder Structure

resume-ranking-nlp/
├── main.py
├── ranking_reporting.py
├── resume_processing.py
├── resumes/ # Place all PDF resumes here
├── Top_resumes_<...>.csv # Output will be saved here

---

## 🛠️ Requirements

Install dependencies:

pip install pdfplumber spacy scikit-learn
python -m spacy download en_core_web_sm

---

## 📌 Usage

1. Place all resume PDFs inside the resumes/ folder.

2. Edit the job title and job description in main.py.

3. Run the script:

python main.py


---

🧪 Example

🔹 Ranked Resumes Based on Relevance:
1. john_doe.pdf - Score: 85.23%
2. jane_smith.pdf - Score: 72.45%

Top terms in best matching resume: ['data', 'analysis', 'sql', 'python', 'tableau', 'insight'...]

---

📌 Use Case

This tool can help:

HR professionals shortlist relevant resumes faster.

Developers build intelligent filtering into job portals or recruitment systems.

Anyone looking to apply NLP to a real-world task.

---

🧠 Tech Stack

Python

spaCy (en_core_web_sm)

pdfplumber

scikit-learn (TF-IDF, cosine similarity)

📄 License
This project is open-source under the MIT License.

---

🙌 Contributions

Pull requests are welcome. For major changes, please open an issue first.

---

✨ Future Improvements

GUI with Streamlit or Flask

Add support for DOCX resumes

Use deep learning models (e.g., BERT embeddings)

Ranking explanation dashboard

---

Let me know if you want this converted to a downloadable `.md` file or tailored further with project screenshots, links, or demo GIFs.

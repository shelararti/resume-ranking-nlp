# 📊 Resume Ranking System using NLP

This Python-based project ranks PDF resumes based on their relevance to a specific job description using **Natural Language Processing (NLP)** techniques. It's designed for HR teams, recruiters, or developers looking to build AI-powered applicant tracking tools.

---

## 🎯 What It Does

📄 PDF Text Extraction: Grabs content from multiple resumes with pdfplumber

🧠 Smart Text Cleaning: Preps text with spaCy — lemmatizes, removes noise (stopwords), and gets it ready for analysis

📊 Vectorization & Comparison: Turns resumes and job description into TF-IDF vectors, compares them using cosine similarity

🥇 Rank & Report: Outputs a ranked list of resumes, saves results as CSV for easy sharing

🔍 Insight Spotlight: Shows the top keywords from the top-scoring resume



---

## 🗂️ Project Setup — Folder Layout

resume-ranking-nlp/

│

├── main.py                   # 🚦 Entry point — run this!

├── ranking_reporting.py      # 📝 Reporting & ranking logic

├── resume_processing.py      # 📑 Resume parsing & preprocessing

├── resumes/                  # 📂 Drop all PDF resumes here

└── Top_resumes_<timestamp>.csv  # 🏆 Output saved here


---

## 🛠️ Requirements

Install dependencies:

`pip install pdfplumber spacy scikit-learn`

`python -m spacy download en_core_web_sm`

---

## ⚡ How to Use

📂 Put all the PDF resumes you want to rank inside the resumes/ folder.

✍️ Customize your target job title and job description in main.py.

🚀 Run the ranking engine:

   `python main.py`


---

## 🧪 Sample Output

Top-ranked resumes by relevance:

1️⃣ john_doe.pdf — Score: 85.23%

2️⃣ jane_smith.pdf — Score: 72.45%

Key skills spotlight:
['data', 'analysis', 'sql', 'python', 'tableau', 'insight'...]

---

## 💼 Who Benefits?

🧑‍💼 HR pros speeding up candidate screening

👨‍💻 Developers building smarter job portals or ATS systems

🤓 NLP enthusiasts solving real-world challenges

---

## 🧰 Tech Stack

🐍 Python

💡 spaCy (en_core_web_sm)

📄 pdfplumber

📈 scikit-learn (TF-IDF, cosine similarity)

---

## 📜 License
This project is open-source under the MIT License.

---

## 🙌 Contributions

Pull requests are welcome. For major changes, please open an issue first.

---

## 🔮 Future Improvements

🎨 GUI with Streamlit or Flask

📄 Add support for DOCX resumes

🤖 Use deep learning models (e.g., BERT embeddings)

📊 Ranking explanation dashboard

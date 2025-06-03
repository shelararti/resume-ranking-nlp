import csv
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_resumes(job_description, resumes, job_title):
    # Preprocess job description
    # Note: resumes are already preprocessed here.
    
    documents = [job_description] + list(resumes.values())

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)
    similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])[0]
    
    ranked = sorted(zip(resumes.keys(), similarities), key=lambda x: x[1], reverse=True)
    
    # Display results
    print("\n🔹 Ranked Resumes Based on Relevance:")
    for rank, (name, score) in enumerate(ranked, 1):
        print(f"{rank}. {name} - Score: {score * 100:.2f}%")
    
    # Save CSV
    filename = f"Top_resumes_{job_title.replace(' ', '_')}_{datetime.now().strftime('%Y_%m_%d')}.csv"
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Rank", "Filename", "Score (%)"])
        for rank, (name, score) in enumerate(ranked, 1):
            writer.writerow([rank, name, f"{score * 100:.2f}"])
    
    # Extract top terms from best resume
    top_resume_name = ranked[0][0]
    top_resume_text = resumes[top_resume_name]
    tfidf_top = vectorizer.transform([top_resume_text])
    top_terms = sorted(zip(vectorizer.get_feature_names_out(), tfidf_top.toarray()[0]), key=lambda x: -x[1])[:10]
    print(f"\nTop terms in best matching resume: {[term for term, _ in top_terms]}")

    return ranked

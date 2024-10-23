import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
from heapq import nlargest
from spacy.cli import download

# Load spaCy English model
model_name = 'en_core_web_sm'
try:
    nlp = spacy.load(model_name)
except OSError:
    print(f"Model '{model_name}' not found. Downloading...")
    download(model_name)
    nlp = spacy.load(model_name)


def clean_text(text):
    """
    Cleans the input text by removing stopwords and special characters using spaCy.
    """
    doc = nlp(text.lower())
    cleaned_words = [
        token.lemma_ for token in doc if not token.is_stop and not token.is_punct and not token.is_digit
    ]
    return ' '.join(cleaned_words)

def summarize_text(text, max_sentences=3):
    """
    Summarizes the input text by extracting key sentences based on word frequency.
    Args:
        text (str): The full text to summarize.
        max_sentences (int): Maximum number of summary sentences.
    Returns:
        str: The summary text.
    """
    doc = nlp(text)
    sentences = list(doc.sents)

    if len(sentences) <= max_sentences:
        return text

    cleaned_text = clean_text(text)
    word_frequencies = Counter(cleaned_text.split())

    max_frequency = max(word_frequencies.values())
    for word in word_frequencies:
        word_frequencies[word] /= max_frequency

    sentence_scores = {}
    for sent in sentences:
        sentence_text = sent.text.lower()
        for word in word_frequencies:
            if word in sentence_text:
                if sent not in sentence_scores:
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]

    summary_sentences = nlargest(max_sentences, sentence_scores, key=sentence_scores.get)
    return ' '.join([sent.text for sent in summary_sentences])

def extract_keywords_tfidf(corpus, max_keywords=10):
    """
    Extracts keywords using TF-IDF from a corpus.
    Args:
        corpus (list): List of documents.
        text (str): Text for which keywords are to be extracted.
        max_keywords (int): Maximum number of keywords to extract.
    Returns:
        list: A list of extracted keywords.
    """
    # Initialize TF-IDF Vectorizer
    vectorizer = TfidfVectorizer(stop_words='english', max_features=max_keywords)

    # Fit the vectorizer on the entire corpus and transform the specific document
    tfidf_matrix = vectorizer.fit_transform(corpus)
    feature_names = vectorizer.get_feature_names_out()

    # Get the feature indices sorted by TF-IDF score
    tfidf_scores = tfidf_matrix.toarray()[0]
    top_indices = tfidf_scores.argsort()[-max_keywords:][::-1]

    # Extract the corresponding feature names (keywords)
    keywords = [feature_names[index] for index in top_indices]

    return keywords


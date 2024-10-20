import streamlit as st
from pdf_processor import extract_text_from_pdf
from text_processor import clean_text, summarize_text, extract_keywords_tfidf

# Streamlit app title
st.title("PDF Text Processing and Summarization")

# File uploader for PDF files
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Save the uploaded file temporarily
    with open("temp_pdf.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Process the uploaded PDF file
    extracted_text = extract_text_from_pdf("temp_pdf.pdf")

    # Check if text extraction was successful
    if extracted_text:

        # Word count
        word_count = len(extracted_text.split())
        st.markdown(f"**Word Count:** {word_count}")

        # Clean and summarize the text
        cleaned_text = clean_text(extracted_text)

        # Input for number of sentences in summary
        max_sentences = st.slider("Select number of summary sentences:", min_value=1, max_value=5, value=3)

        summary = summarize_text(extracted_text, max_sentences=max_sentences)


        st.header("Summary")
        st.write(summary)

        # Extract keywords
        # Use a small corpus for demonstration; you can modify this as needed
        corpus = ["This is a sample document.", "Another document for keyword extraction."]
        keywords = extract_keywords_tfidf(corpus, extracted_text, max_keywords=10)

        st.header("Extracted Keywords")
        st.write(keywords)

        # Provide download option for the summary
        st.download_button("Download Summary", summary, file_name="summary.txt", mime="text/plain")
    else:
        st.error("Failed to extract text from the uploaded PDF.")

# Instructions for using the app
st.sidebar.header("Instructions")
st.sidebar.write(
    "1. Upload a PDF file using the uploader above. \n"
    "2. The app will extract text and metadata from the PDF. \n"
    "3. You will see the cleaned text, a summary of the text, and the extracted keywords.\n"
    "4. Use the slider to adjust the number of sentences in the summary."
)

# Optional: Add footer
st.sidebar.markdown("---")
st.sidebar.write("Created by Dronesh Magare - AI Internship Task")

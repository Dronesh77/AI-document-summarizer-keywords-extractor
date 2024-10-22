# Integrated streamlit app
############################################################################################################################################
import os
import streamlit as st
from concurrency_manager import ConcurrencyManager
import logging
# import tempfile

# Configure logging
log_file_path = 'Y:/AI_Internship_Task_Wasserstoff/logs/process.log'
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)  # Create directory if it doesn't exist

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_info(message):
    logging.info(message)
    st.write(message)  # Display in Streamlit

def log_error(message):
    logging.error(message)
    st.error(message)  # Display error in Streamlit

def save_uploaded_file(uploadedfile, directory):
    """
    Save an uploaded file to a directory.
    """
    file_path = os.path.join(directory, uploadedfile.name)
    with open(file_path, 'wb') as f:
        f.write(uploadedfile.getbuffer())
    return file_path

def main():
    st.title("PDF Metadata Extraction App")

    # Input: File uploader to simulate folder upload (multiple files)
    uploaded_files = st.file_uploader("Upload PDFs from Folder", type=["pdf"], accept_multiple_files=True)

    if uploaded_files:
        # Create a temporary directory to store uploaded files
        temp_dir = '/tmp/'
        file_paths = []

        # Ensure the directory exists
        os.makedirs(temp_dir, exist_ok=True)
            
        # Save each uploaded file to the temporary directory
        for uploaded_file in uploaded_files:
            file_path = save_uploaded_file(uploaded_file, temp_dir)
            log_info(f"Saved file: {file_path}")
            file_paths.append(file_path)

            # Initialize Concurrency Manager
            manager = ConcurrencyManager(temp_dir)

            if st.button('Process PDFs'):
                # Process each uploaded PDF individually using manager.process_pdf
                log_info("Processing started...")
                for pdf_path in file_paths:
                    result = manager.process_pdf(pdf_path)  # Process each PDF
                    if result:
                        # Extract results for each PDF
                        pdf_file_name = os.path.basename(result['filename'])
                        keywords = result['keywords']
                        summary_id = result['mongodb_id']
                        metadata = result['metadata']
                        summary = result['summary']  # Assuming you have 'summary' in your result

                        # Display results in Streamlit
                        st.write(f"### PDF File: {pdf_file_name}")
                        st.write(f"**Keywords**: {', '.join(keywords)}")
                        st.write(f"**Summary**: {summary}")
                        st.write(f"**Summary ID (in MongoDB)**: {summary_id}")
                        st.write(f"**Metadata**: {metadata}")
                    else:
                        st.error(f"Failed to process {pdf_path}")
                st.success("Processing completed!")

    else:
        st.info("Please upload PDF files from the folder to process.")

if __name__ == "__main__":
    main()





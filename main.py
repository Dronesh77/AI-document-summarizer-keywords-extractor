import streamlit as st
from concurrency_manager import ConcurrencyManager
import logging
import os
import traceback

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

def main():
    st.title("PDF Metadata Extraction App")

    # Input: File uploader to upload multiple PDFs
    uploaded_files = st.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)

    manager = ConcurrencyManager()
    if st.button('Process PDFs'):

        for file in uploaded_files:

            if file:  
                log_info(f"Processing started...: {file.name}")
                
                try:
                    result = manager.process_pdf(file)  
                    st.write(result)

                except:
                    st.error(f"Failed to process {file}")
                    print("\n\n\n\n")
                    print(traceback.print_exc())

            else:
                st.info("Please upload PDF files to process.")

if __name__ == "__main__":
    main()






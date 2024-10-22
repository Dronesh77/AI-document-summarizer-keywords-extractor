import concurrent.futures
import pdf_processor
import text_processor  
from mongodb_handler import MongoDBHandler
import nltk  
from nltk.tokenize import sent_tokenize
import os
import logging
import traceback
import utils


nltk.download('punkt_tab')

class ConcurrencyManager:
    def __init__(self, pdf_directory):
        self.pdf_directory = pdf_directory

    def process_pdf(self, pdf_path):
        """Process a single PDF file and return its summary."""

        try:
            db_handler = MongoDBHandler()
            query = {"file_name": pdf_path}

            if db_handler.check_document_exists(query):
                return None
            else:

                print(f"Processing {pdf_path}...")

                # Extract text from the PDF file using pdf_processor
                extracted_text = pdf_processor.extract_text_from_pdf(pdf_path)

                if extracted_text:
                    # Tokenize the extracted text into sentences
                    sentences = sent_tokenize(extracted_text)

                    # Create a corpus as a list of sentences
                    corpus = sentences  # Now corpus is a list of sentences

                    # Generate the summary using text_processor
                    summary = text_processor.summarize_text(extracted_text)
                    keywords = text_processor.extract_keywords_tfidf(corpus,extracted_text)

                    metadata = utils.get_file_metadata(pdf_path)

                    summary_id = db_handler.insert_summary_with_keywords(summary, keywords, pdf_path,metadata)


                    # Return the summary (instead of saving the full text)
                    return {
                        "filename": pdf_path,
                        "summary": summary,
                        "keywords":keywords,
                        "mongodb_id":summary_id,
                        "metadata":metadata
                    }
                
                else:
                    print(f"Failed to extract text from {pdf_path}.")
                    return None
            
        except Exception as e:
            print(f"Error processing {pdf_path}: {e}")
            return None

    # def process_all_pdfs(self):

    #     try:

    #         """Process all PDF files in the specified directory concurrently."""
    #         pdf_files = [f for f in os.listdir(self.pdf_directory) if f.endswith('.pdf')]
    #         print(f"Found PDF files: {pdf_files}")
            
    #         if not pdf_files:
    #             print("No PDF files found in the directory.")
    #             return []

    #         with concurrent.futures.ThreadPoolExecutor() as executor:
    #             # This will pass each file name to the process_pdf method
    #             results = list(executor.map(self.process_pdf, pdf_files))

    #         return results
        

        except:
            logging.error(traceback.format_exc())
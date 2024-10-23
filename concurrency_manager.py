import pdf_processor
import text_processor  
from mongodb_handler import MongoDBHandler
from nltk.tokenize import sent_tokenize
import logging
import traceback
import utils



class ConcurrencyManager:

    def process_pdf(self,file):
        """Process a single PDF file and return its summary."""

        try:
            # Extract text from the PDF file using pdf_processor
            extracted_text = pdf_processor.extract_text_from_pdf(file)
            
            if extracted_text:
                # Tokenize the extracted text into sentences
                sentences = sent_tokenize(extracted_text)

                # Create a corpus as a list of sentences
                corpus = sentences  
                return{
                    "keywrods": corpus
                }
                # Generate the summary using text_processor
                summary = text_processor.summarize_text(extracted_text)
                
                keywords = text_processor.extract_keywords_tfidf(corpus)

                metadata = utils.get_file_metadata(file)
            
                db_handler = MongoDBHandler()
                summary_id = db_handler.insert_summary_with_keywords(summary, keywords, file ,metadata) 
                
                # Return the summary 
                return {
                        "filename": file.name,
                        "summary": summary,
                        "keywords":keywords,
                        "mongodb_id":summary_id,
                        "metadata":metadata
                    }
                
            else:
                print(f"Failed to extract text from {file.name}.")
                return "process_pdf failed"
            
        except Exception as e:
            print(f"Error processing {file.name}: {e}")
            return "can't process pdf"
        

        except:
            logging.error(traceback.format_exc())




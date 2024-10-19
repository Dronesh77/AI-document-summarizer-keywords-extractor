import concurrent.futures
import pdf_processor
import text_processor  
import os

class ConcurrencyManager:
    def __init__(self, pdf_directory, output_directory):
        self.pdf_directory = pdf_directory
        self.output_directory = output_directory

    def process_pdf(self, pdf_file):
        """Process a single PDF file and return its summary."""
        try:
            print(f"Processing {pdf_file}...")

            # Extract text from the PDF file using pdf_processor
            pdf_path = os.path.join(self.pdf_directory, pdf_file)
            extracted_text = pdf_processor.extract_text_from_pdf(pdf_path)

            if extracted_text:
                # Generate the summary using text_processor
                summary = text_processor.summarize_text(extracted_text)

                # Return the summary (instead of saving the full text)
                return {
                    "filename": pdf_file,
                    "summary": summary
                }
            else:
                print(f"Failed to extract text from {pdf_file}.")
                return None
        except Exception as e:
            print(f"Error processing {pdf_file}: {e}")
            return None

    def process_all_pdfs(self):
        """Process all PDF files in the specified directory concurrently."""
        pdf_files = [f for f in os.listdir(self.pdf_directory) if f.endswith('.pdf')]
        print(f"Found PDF files: {pdf_files}")
        
        if not pdf_files:
            print("No PDF files found in the directory.")
            return []

        with concurrent.futures.ThreadPoolExecutor() as executor:
            # This will pass each file name to the process_pdf method
            results = list(executor.map(self.process_pdf, pdf_files))

        return results

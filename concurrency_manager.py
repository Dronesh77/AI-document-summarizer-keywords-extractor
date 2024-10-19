import concurrent.futures
import pdf_processor  
import os                         ###  Y:\AI Internship Task Wasserstoff\dataset\pdf1.pdf

class ConcurrencyManager:
    def __init__(self, pdf_directory,output_directory):
        self.pdf_directory = pdf_directory
        self.output_directory = output_directory

    def process_all_pdfs(self):
        """Process all PDF files in the specified directory concurrently."""
        pdf_files = [f for f in os.listdir(self.pdf_directory) if f.endswith('.pdf')]
        print(f"Found PDF files: {pdf_files}")
        with concurrent.futures.ThreadPoolExecutor() as executor:
          
            results = pdf_processor.process_pdfs(self.pdf_directory, self.output_directory)
        
        return results

    # def process_pdf(self, pdf_file):
    #     """Process a single PDF file."""
    #     try:
    #         print(f"Processing {pdf_file}...")
    #         # Call your PDF processing function here
    #         pdf_path = os.path.abspath(os.path.join(self.pdf_directory, pdf_file))

    #         # print(f"Full path: {pdf_path}")  # Check full path 
    #         result = pdf_processor.process_pdfs(self.pdf_directory, self.output_directory)
    #         return result
    #     except Exception as e:
    #         print(f"Error processing {pdf_file}: {e}")
    #         return None

# # Example usage:
# if __name__ == "__main__":
#     pdf_dir = "Y:\AI_Internship_Task_Wasserstoff\dataset"  # Change this path as necessary
#     output_dir = "Y:\AI_Internship_Task_Wasserstoff\output" # Change this path as necessary
#     manager = ConcurrencyManager(pdf_dir,output_dir)
    
#     # Process all PDFs and retrieve results
#     results = manager.process_all_pdfs()
#     print("Processing completed. Results:")
#     for result in results:
#         print(result)

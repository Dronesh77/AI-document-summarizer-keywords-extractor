import os
import PyPDF2
from utils import log_info, log_error, is_pdf, get_file_metadata

# Function to extract text from a single PDF
def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.
    :param pdf_path: Path to the PDF file.
    :return: Extracted text as a string, or None if an error occurs.
    """
    if not is_pdf(pdf_path):
        log_error(f"File {pdf_path} is not a valid PDF.")
        return None

    try:
        with open(pdf_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page_num in range(len(reader.pages)):
                text += reader.pages[page_num].extract_text()
            log_info(f"Successfully extracted text from {pdf_path}.")
            return text
    except Exception as e:
        log_error(f"Error extracting text from {pdf_path}: {str(e)}")
        return None

# Function to process a directory of PDFs
# def process_pdf_directory(directory_path, output_dir):
#     """
#     Processes all PDFs in a directory, extracts text, and saves the results.
#     :param directory_path: Directory containing PDF files.
#     :param output_dir: Directory where extracted text files will be saved.
#     """
#     if not os.path.exists(directory_path):
#         log_error(f"Directory {directory_path} does not exist.")
#         return

#     # Create output directory if not exists
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)

#     for filename in os.listdir(directory_path):
#         file_path = os.path.join(directory_path, filename)
#         if is_pdf(file_path):
#             # Extract text from the PDF
#             extracted_text = extract_text_from_pdf(file_path)
#             if extracted_text:
#                 # Save the extracted text to a file
#                 output_file = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.txt")
#                 with open(output_file, 'w', encoding='utf-8') as f:
#                     f.write(extracted_text)
#                 log_info(f"Saved extracted text from {filename} to {output_file}.")
#             else:
#                 log_error(f"Failed to extract text from {file_path}.")
#         else:
#             log_info(f"Skipping non-PDF file: {file_path}")

# # Example usage
# if __name__ == "__main__":
#     pdf_directory = "Y:/AI Internship Task Wasserstoff/dataset"  # Path to your PDF files
#     output_directory = "Y:/AI Internship Task Wasserstoff/output"  # Define where to save outputs

#     process_pdfs(pdf_directory, output_directory)

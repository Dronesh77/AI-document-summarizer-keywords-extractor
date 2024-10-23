import PyPDF2



def extract_text_from_pdf(pdf_file):
    # Create a PDF reader object
    try:
        
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        # Check if PDF is encrypted
        if pdf_reader.is_encrypted:
            return "Error: PDF is encrypted"
            
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
        return text
        
    except Exception as e:
        return f"Error processing PDF: {str(e)}"




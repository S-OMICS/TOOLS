#Install PyPDF2
#pip install PyPDF2

from PyPDF2 import PdfMerger
import os

def merge_pdfs(pdf_files, output_file):
    # Initialize PdfMerger object
    merger = PdfMerger()
    
    # Add each PDF to the merger
    for pdf in pdf_files:
        merger.append(pdf)
    
    # Save the merged PDF to the specified output path
    merger.write(output_file)
    merger.close()

if __name__ == "__main__":
    # List of PDF files to merge
    pdf_files = [
        "C:/Users/pshri/Desktop/COMMON/Documents/M Tech degree.pdf",
        "C:/Users/pshri/Desktop/COMMON/Documents/B Tech degree.pdf",
        "C:/Users/pshri/Desktop/COMMON/Documents/Language Certificate.pdf"
    ]
    
    # Output file location and name
    output_file = "C:/Users/pshri/Desktop/COMMON/Documents/merged_output.pdf"
    
    # Check if output directory exists
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Call the merge_pdfs function
    merge_pdfs(pdf_files, output_file)
    print(f"PDFs merged successfully! Output saved to {output_file}")

import streamlit as st
import os
import base64
from pathlib import Path

def copy_to_clipboard(text):
    """Function to update session state with copied text"""
    st.session_state.copied_text = text

def list_pdfs(directory):
    """Returns a sorted list of PDF file paths and generates clean labels."""
    pdf_path = Path(directory)
    pdf_files = sorted([str(file) for file in pdf_path.glob("*.pdf")])
    labels = [f"PDF {i+1}" for i in range(len(pdf_files))]  # Generate labels like "PDF 1", "PDF 2", ...
    return pdf_files, labels

def show_pdf(pdf_path):
    """Displays a PDF in an embedded viewer without showing file name."""
    with open(pdf_path, "rb") as pdf_file:
        pdf_data = pdf_file.read()
        base64_pdf = base64.b64encode(pdf_data).decode("utf-8")
        
        # Embedded PDF viewer without filename
        pdf_display = f"""
        <div style="display: flex; justify-content: center;">
            <iframe 
                src="data:application/pdf;base64,{base64_pdf}" 
                width="700" height="500" 
                style="border: none;" 
            ></iframe>
        </div>
        <style>
            iframe::-webkit-scrollbar {{
                display: none;  /* Hide scrollbar */
            }}
            iframe {{
                overflow: hidden;
                border: none;
            }}
        </style>
        """
        st.markdown(pdf_display, unsafe_allow_html=True)
        
def get_images(image_folder):
    """Returns a list of image file paths from the given folder."""
    images = sorted([os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith((".png", ".jpg", ".jpeg"))])
    return images
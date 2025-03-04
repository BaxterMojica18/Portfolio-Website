import streamlit as st
import os
import base64
from pathlib import Path

def copy_to_clipboard(text):
    """Function to update session state with copied text"""
    st.session_state.copied_text = text

def list_pdfs(directory):
    """Returns a sorted list of PDF file paths and generates clean labels."""
    pdf_path = Path(__file__).parent / directory  # Get absolute path
    pdf_files = sorted([str(file) for file in pdf_path.glob("*.pdf")])
    labels = [f"PDF {i+1}" for i in range(len(pdf_files))]  
    return pdf_files, labels

def show_pdf(pdf_path):
    """Displays a PDF via Streamlit's static file serving."""
    with open(pdf_path, "rb") as pdf_file:
        st.download_button(label="📄 Download PDF", data=pdf_file, file_name=Path(pdf_path).name, mime="application/pdf")
    
    st.markdown(f'<iframe src="{pdf_path}" width="700" height="500"></iframe>', unsafe_allow_html=True)

        
def get_images(image_folder):
    """Returns a list of image file paths from the given folder."""
    images = sorted([os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith((".png", ".jpg", ".jpeg"))])
    return images
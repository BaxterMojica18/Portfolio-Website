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

import streamlit as st
import base64
from pathlib import Path

def show_pdf(pdf_path):
    """Displays a PDF using Streamlit components (fixing infinite loading)."""
    
    # Check if file exists
    if not Path(pdf_path).is_file():
        st.error("Error: PDF file not found!")
        return
    
    with open(pdf_path, "rb") as pdf_file:
        pdf_data = pdf_file.read()
        base64_pdf = base64.b64encode(pdf_data).decode("utf-8")

    # Provide a download button
    st.download_button(
        label="📄 Download PDF",
        data=pdf_data,
        file_name=Path(pdf_path).name,
        mime="application/pdf",
    )

    # Use iframe to load the PDF properly
    pdf_display = f"""
    <iframe 
        src="data:application/pdf;base64,{base64_pdf}" 
        width="700" height="500" 
        style="border: none;"
    ></iframe>
    """
    
    # Display the PDF in the Streamlit app
    st.components.v1.html(pdf_display, height=500, scrolling=True)


        
def get_images(image_folder):
    """Returns a list of image file paths from the given folder."""
    images = sorted([os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith((".png", ".jpg", ".jpeg"))])
    return images
import streamlit as st
import os
import requests
from pathlib import Path
from streamlit_pdf_viewer import pdf_viewer

def list_pdfs(directory):
    """Returns a sorted list of PDF file paths and generates clean labels."""
    pdf_path = Path(directory)
    pdf_files = sorted([str(file) for file in pdf_path.glob("*.pdf")])
    labels = [f"PDF {i+1}" for i in range(len(pdf_files))]  # Generate labels like "PDF 1", "PDF 2", ...
    return pdf_files, labels

def get_drive_pdf_links(folder_link):
    """Fetches PDF file links from a shared Google Drive folder."""
    folder_id = folder_link.split("/")[-1].split("?")[0]  # Extract folder ID
    drive_api_url = f"https://www.googleapis.com/drive/v3/files?q='{folder_id}'+in+parents&key={st.secrets['GOOGLE_API_KEY']}&fields=files(id,name)"

    try:
        response = requests.get(drive_api_url)
        if response.status_code == 200:
            files = response.json().get("files", [])
            pdf_links = {file["name"]: f"https://drive.google.com/uc?export=view&id={file['id']}" for file in files if file["name"].endswith(".pdf")}
            return pdf_links
        else:
            st.error("Failed to fetch files from Google Drive. Check API Key and folder permissions.")
            return {}
    except Exception as e:
        st.error(f"Error fetching PDFs: {e}")
        return {}

def show_local_pdf(pdf_path):
    """Displays a local PDF centered using streamlit_pdf_viewer."""
    with open(pdf_path, "rb") as file:
        binary_data = file.read()

    # Center the PDF using custom HTML & CSS
    st.markdown(
        """
        <style>
        .pdf-container {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Use a div wrapper for centering
    st.markdown('<div class="pdf-container">', unsafe_allow_html=True)
    pdf_viewer(input=binary_data, width=700)
    st.markdown("</div>", unsafe_allow_html=True)

def get_images(image_folder):
    """Returns a list of image file paths from the given folder."""
    images = sorted([os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith((".png", ".jpg", ".jpeg"))])
    return images

def get_images1(image_folder):
    """Returns a list of image file paths from the given folder."""
    images = sorted([os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith((".png", ".jpg", ".jpeg"))])
    return images


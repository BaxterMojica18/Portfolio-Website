import streamlit as st
import os
import base64
from pathlib import Path
import os
from dotenv import load_dotenv

# Load .env.local
load_dotenv(".env.local")

# Access environment variables
credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
sheet_id = os.getenv("SHEET_ID")

print("Credentials Path:", credentials_path)
print("Google Sheet ID:", sheet_id)

def copy_to_clipboard(text):
    """Function to update session state with copied text"""
    st.session_state.copied_text = text

def list_pdfs(directory):
    """Returns a sorted list of PDF file paths and generates clean labels."""
    pdf_path = Path(__file__).parent / directory  # Get absolute path
    pdf_files = sorted([str(file) for file in pdf_path.glob("*.pdf")])
    labels = [f"PDF {i+1}" for i in range(len(pdf_files))]  
    return pdf_files, labels

def get_drive_pdf_links(folder_link):
    """Extracts file links from a shared Google Drive folder."""
    folder_id = folder_link.split("/")[-1].split("?")[0]  # Extract folder ID
    drive_api_url = f"https://www.googleapis.com/drive/v3/files?q='{folder_id}'+in+parents&key={st.secrets['GOOGLE_API_KEY']}&fields=files(id,name)"

    try:
        import requests
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

def show_pdf(pdf_url):
    """Embeds a Google Drive PDF in an iframe."""
    pdf_display = f"""
    <iframe 
        src="{pdf_url}" 
        width="700" height="500" 
        style="border: none;"
    ></iframe>
    """
    st.markdown(pdf_display, unsafe_allow_html=True)
def get_images(image_folder):
    """Returns a list of image file paths from the given folder."""
    images = sorted([os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith((".png", ".jpg", ".jpeg"))])
    return images
import streamlit as st
from functions import get_drive_pdf_links, show_pdf

# Google Drive shared folder links
COURSERA_FOLDER_LINK = "https://drive.google.com/drive/folders/1ma-BnhXI3xQsmeY1GYCuGtPNJmCpLL1V?usp=sharing"
LINKEDIN_FOLDER_LINK = "https://drive.google.com/drive/folders/1v8jaHHequOx6yhVGXcM6wmUxdZI1SczS?usp=sharing"

def certificates():
    st.title("📜 Certificates")
    st.write("Browse my certifications and achievements below.")

    # Fetch PDFs from Google Drive
    coursera_pdfs = get_drive_pdf_links(COURSERA_FOLDER_LINK)
    linkedin_pdfs = get_drive_pdf_links(LINKEDIN_FOLDER_LINK)

    # Coursera Dropdown
    if coursera_pdfs:
        st.subheader("🎓 Coursera Certificates")
        selected_coursera = st.selectbox("Select a Coursera Certificate", list(coursera_pdfs.keys()), key="coursera_dropdown")
        show_pdf(coursera_pdfs[selected_coursera])

    # LinkedIn Dropdown
    if linkedin_pdfs:
        st.subheader("🔗 LinkedIn Certificates")
        selected_linkedin = st.selectbox("Select a LinkedIn Certificate", list(linkedin_pdfs.keys()), key="linkedin_dropdown")
        show_pdf(linkedin_pdfs[selected_linkedin])

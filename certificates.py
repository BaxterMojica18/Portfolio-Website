import streamlit as st
from functions import list_pdfs, show_pdf

def certificates():
    st.title("📜 Certificates")
    st.write("Browse my certifications and achievements below.")

    # Get lists of PDFs and their labels
    coursera_pdfs, coursera_labels = list_pdfs("certificates/Coursera")
    linkedin_pdfs, linkedin_labels = list_pdfs("certificates/LinkedIn")

    # Coursera Dropdown
    if coursera_pdfs:
        st.subheader("🎓 Coursera Certificates")
        selected_coursera = st.selectbox("Select a Coursera Certificate", coursera_labels, key="coursera_dropdown")
        show_pdf(coursera_pdfs[coursera_labels.index(selected_coursera)])

    # LinkedIn Dropdown
    if linkedin_pdfs:
        st.subheader("🔗 LinkedIn Certificates")
        selected_linkedin = st.selectbox("Select a LinkedIn Certificate", linkedin_labels, key="linkedin_dropdown")
        show_pdf(linkedin_pdfs[linkedin_labels.index(selected_linkedin)])
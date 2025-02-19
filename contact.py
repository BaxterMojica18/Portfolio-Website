import streamlit as st
import time as time

def contact():
    st.title("Contact Me")
    st.write("Feel free to reach out. My contact details are below.")

    # Email section with a smaller text area
    st.text_area("My Email", "baxterdavid.mojica@gmail.com", height=68)

    # Phone section with a smaller text area
    st.text_area("My Number", "0967 284 1554", height=68)

    st.write("")
    st.text("You can also download my CV below for more details about me.")

    # Open the PDF file and create a download button
    with open("Baxter_Mojica_CV.pdf", "rb") as file:
        pdf_bytes = file.read()
        
    success_message = st.empty()

    download_pdf = st.download_button(
        label="Download PDF",
        data=pdf_bytes,
        file_name="Baxter_Mojica_CV.pdf",
        mime="application/pdf",
    )

    if download_pdf:
        success_message.success("PDF downloaded successfully!")
        time.sleep(6)  # Wait for 6 seconds
        success_message.empty()  # Clear the message
import streamlit as st
from functions import show_local_pdf

with open("files/Baxter_Mojica_CV.pdf", "rb") as file:
    cv_bytes = file.read()

def cv():
    st.title("📜 My Curriculum Vitae (CV)")
    col1, col2, col3 = st.columns([1, 3, 1])  # Middle column is wider
    with col2:
        show_local_pdf('files/Baxter_Mojica_CV.pdf')
        
    st.subheader("Links")
    st.write("Portfolio Link (This Portfolio): https://portfolio-website-zky9fhygba8p2qgnvfegdx.streamlit.app/ ")
    st.write("")
    st.write("LinkedIn Profile: https://www.linkedin.com/in/baxter-mojica-profile/")
    st.write("")
    st.write("GitHub Profile: https://github.com/BaxterMojica18")
    st.write("")
    st.write("Work Email: baxterdavid.mojica@gmail.com")
    st.write("")
    st.text_area("My Number", "0967 284 1554", height=68)
    st.write("")
    st.write("Download my CV Below")
    st.download_button(
        label="📄 Download CV",
        data=cv_bytes,
        file_name="Baxter_Mojica_CV.pdf",
        mime="application/pdf"
    )
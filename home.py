import streamlit as st

def home():
    # Center the title using HTML & CSS
    st.title("Welcome to My Portfolio")
    st.write("")

    # Add adjustable spacing below `st.write`
    st.write("Feel free to explore here as everything about me including my achievements and experiences are here. Enjoy! :)")
     # Empty write adds a small space
    st.markdown("<div style='margin-bottom: 30px;'></div>", unsafe_allow_html=True)  # Adjust spacing

    # Layout with two columns
    col1, col2 = st.columns([1, 2])  # Adjust width ratios as needed

    with col1:
        st.image("images/me.jpg", use_container_width=True)  # Fix the image path

    with col2:
        st.text_area("About Me", "I am Jehran Baxter David M. Mojica, a BS in Computer Engineering graduate from De La Salle University - Dasmarinas last 2024. I mainly focus on developing technologies using Python as the main programming language and use Machine Learning models to create solutions. I often make Computer Vision projects using Yolo.", height=150)
        st.text_area("My Career Path Goal", "I want to start and continue in the field as a Python Engineer, hopefully going to reach the level of an ML Engineer pursuing the path to AI Engineer someday. ")

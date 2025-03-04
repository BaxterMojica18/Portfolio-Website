import streamlit as st
import os
from PIL import Image

from functions import get_images


def portfolio():
    st.title("Portfolio")
    st.write("These are the projects that I have done along with some of my work experience showcases here.")

    # Thesis Project
    st.subheader("Thesis Project")
    st.write("This is my thesis project during my college years back last 2024. In our group I was the programmer who created the thesis and made it work, utilizing Python, and using an external or the built-in camera of the chosen device to detect Filipino Sign Language Gestures and convert them to speech for the mute to hear.")

    # Image Slideshow
    st.subheader("Project Images")

    image_folder = "images/thesis"
    images = get_images(image_folder)

    if images:
        # Initialize session state
        if "image_index" not in st.session_state:
            st.session_state.image_index = 0

        num_images = len(images)
        current_index = st.session_state.image_index

        # Load and resize the image to 1280x720
        image = Image.open(images[current_index])
        image = image.resize((1280, 720))  # Resize to exact 1280x720

        # Centered Image Display
        st.markdown(
            """
            <style>
                .image-container {
                    display: flex;
                    justify-content: center;
                }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.image(image, width=1280)  # Display resized image
        st.markdown("</div>", unsafe_allow_html=True)

        # Shortened & Centered Progress Bar
        progress = (current_index + 1) / num_images  # Normalize between 0 and 1
        col1, col2, col3 = st.columns([2, 3, 2])  # Centered progress bar
        with col1:
            st.write("")
        with col2:
            st.progress(progress)  # Shortened width
        with col3:
            st.write("")

        # Centered Navigation Buttons
        col1, col2, col3 = st.columns([2, 1, 2])
        with col1:
            st.write("")  # Left spacer
        with col2:
            col_btn1, col_btn2 = st.columns([1, 1])  # Two equal columns inside center column
            with col_btn1:
                prev_clicked = st.button("⬅ Back", key="prev_img")
            with col_btn2:
                next_clicked = st.button("Next ➡", key="next_img")
        with col3:
            st.write("")  # Right spacer
            
                # Project Demo Section
        st.subheader("Project Demo")

        # Video Demo
        video_path = "Demos/Thesis/thesisdemo1.mp4"
        st.video(video_path)



        # Update image index if buttons are clicked
        if prev_clicked:
            st.session_state.image_index = (current_index - 1) % num_images  # Loop back to last image if at start
        if next_clicked:
            st.session_state.image_index = (current_index + 1) % num_images  # Loop back to first image if at end

    else:
        st.write("No images found in the folder.")

    # Another project (example)
    st.write("")
    st.subheader("College Project: Movie Website")
    st.write("This is another college project where me and my girlfriend which is also my classmate at the time collaborated on making. It is a website where we used 'The Movie Database' or 'TMDB' API and the features that we needed which shows trending movies, new movies, and popular movies. We created the website to be able to work even when we hosted it on Github. Pictures and a demo of the website are shown below. You can see the synopsis of the associated movie and you can also watch its trailer in the website as well.")

    # Image Slideshow
    st.subheader("Project Images")

    image_folder = "images/moviesite"
    images = get_images(image_folder)

    if images:
        # Initialize session state
        if "movie_index" not in st.session_state:
            st.session_state.movie_index = 0

        num_images = len(images)
        current_index = st.session_state.movie_index

        # Load and resize the image to 1280x720
        image = Image.open(images[current_index])
        image = image.resize((1280, 720))  # Resize to exact 1280x720

        # Centered Image and Buttons
        st.markdown(
            """
            <style>
                .image-container {
                    display: flex;
                    justify-content: center;
                }
                .button-container {
                    display: flex;
                    justify-content: center;
                    gap: 20px;
                }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.image(image, width=1280)  # Display resized image
        st.markdown("</div>", unsafe_allow_html=True)

        # Centered Navigation Buttons
        st.markdown('<div class="button-container">', unsafe_allow_html=True)
        
        # Shortened & Centered Progress Bar
        progress = (current_index + 1) / num_images  # Normalize between 0 and 1
        col1, col2, col3 = st.columns([2, 3, 2])  # Centered progress bar
        with col1:
            st.write("")
        with col2:
            st.progress(progress)  # Shortened width
        with col3:
            st.write("")

        # Centered Navigation Buttons
        col1, col2, col3 = st.columns([2, 1, 2])
        with col1:
            st.write("")  # Left spacer
        with col2:
            col_btn1, col_btn2 = st.columns([1, 1])  # Two equal columns inside center column
            with col_btn1:
                prev_clicked1 = st.button("⬅ Back", key="prev_img1")
            with col_btn2:
                next_clicked1 = st.button("Next ➡", key="next_img1")
        with col3:
            st.write("")  # Right spacer
            
        # Project Demo Section
        st.subheader("Project Demo")

        # Video Demo
        video_path = "Demos/Website/websitedemo.mkv"
        st.video(video_path)
        
        st.subheader("Project Details")
        st.write("")
        st.write("All the details of this project can be found on my Github Repository. It is a public repository. The link is given below:")
        st.write("Link: https://github.com/BaxterMojica18/moviewebsite")

        # Update image index if buttons are clicked
        if prev_clicked1:
            st.session_state.movie_index = (current_index - 1) % num_images  # Loop back to last image if at start
        if next_clicked1:
            st.session_state.movie_index = (current_index + 1) % num_images  # Loop back to first image if at end
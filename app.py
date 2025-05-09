import time
import json
import streamlit as st

from home import home
from pathlib import Path
from contact import contact
from portfolio import portfolio
from certificates import certificates
from cv import cv

# Set page configuration at the beginning
st.set_page_config(page_title="My Portfolio", page_icon=":man:", layout="wide")

def main():
    
    # Sidebar navigation
    pages = ["Home", "Portfolio", "Contact Me", "Certificates", "CV"]
    choice = st.sidebar.radio("Pages", pages)
    
    if choice == "Home":
        home()
    elif choice == "Portfolio":
        portfolio()
    elif choice == "Contact Me":
        contact()
    elif choice == "Certificates":
        certificates()
    elif choice == "CV":
        cv()

if __name__ == "__main__":
    main()

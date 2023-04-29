# Core Pkgs
import streamlit as st
import os

# EDA Pkg
import pandas as pd

# Image
from PIL import Image

@st.cache
def load_image(image_file):
	img = Image.open(image_file)
	return img

# Fxn to Save Uploaded File to Directory
def save_uploaded_file(uploadedfile):
	with open(os.path.join("tempDir",uploadedfile.name),"wb") as f:
		f.write(uploadedfile.getbuffer())
	return st.success("Saved file :{} in tempDir".format(uploadedfile.name))

def main ():
    st.title("Multiple File Uploads App")
    menu = ["Home", "About" ]
    choice = st.sidebar.selectbox("Menu",menu)
    if choice == "Home":
        st.subheader ("Upload Multiple Files")
        uploadedfiles = st.file_uploader("Upload Multiple Images", type =['png' , 'jpeg' , 'jpg'],accept_multiple_files=True)
        if uploadedfiles is not None:
            st.write(uploadedfiles)# List
            for imagefile in uploadedfiles:
                st.write(imagefile.name)
                st.image(load_image(imagefile), width=250, height=250)
                # Save Individual File.
                save_uploaded_file(imagefile)
        else:
            st.subheader("About APP")

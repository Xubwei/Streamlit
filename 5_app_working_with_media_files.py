# Core Pkgs
import streamlit as st 

# Working Media Files(videos/images/audio)
# # Display Images
from PIL import Image 
img = Image.open("image_03.jpg")
st.image(img,use_column_width=True)

# # From URL
st.image("https://media.istockphoto.com/photos/innovation-and-science-concept-picture-id1177116437")


# Display Videos
video_file = open("secret_of_success.mp4","rb").read()
st.video(video_file,start_time=35)

# Display Audio/Working with Audio
audio_file = open("song.mp3","rb")
st.audio(audio_file.read(),format='audio/mp3')
























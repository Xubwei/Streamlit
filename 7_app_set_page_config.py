# Core Pkgs
import streamlit as st
# from PIL import Image
# img = Image.open("image_03.jpg")
# Must be the first activity of streamlit

# st.set_page_config(page_title='hello everyone title change!!!') #Before 0.70.0


#Method 1
st.set_page_config(page_title='hello~title change!!!',
	page_icon='😭',layout='wide',
	initial_sidebar_state='collapsed')


# # Method 2:Dictionary
# PAGE_CONFIG = {"page_title":"JCharisTech","page_icon":":smiley","layout":"centered"}
# st.set_page_config(**PAGE_CONFIG)


# # Additional Pkgs

# # Fxns
st.title("Hello Streamlit Lovers ❤️ 😃 😅")
st.sidebar.success("Menu")



# if __name__ == '__main__':
# 	main()
# Core Pkgs
import streamlit as st
import pandas as pd


def main():
    st.title("Salary Calculator")
    menu = ["Home","Dataset","About"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Forms Tutorial")

        #Salary Calucaltor
        #Combine forms + columns
        with st.form(key='cal'):
            col1,col2,col3 = st.columns([3,2,1])

            with col1:
                amount = st.number_input("時薪：")
            with col2:
                hour_per_week = st.number_input("工作幾小時？")
            with col3:
                st.text("Salary")
                submit_salary = st.form_submit_button(label="計算")

        if submit_salary:
            with st.expander("Results"):
                daily = [amount * 8]
                weekly = [amount*hour_per_week]
                df = pd.DataFrame({'hourly':amount,'daily':daily,'weekly':weekly})
                st.dataframe(df)

        #Method 1
        with st.form(key='forml'):
                firstname = st.text_input("firstname：")
                lastname = st.text_input("lastname：")
                dob = st.date_input("Date of Birth")

                submit_button = st.form_submit_button(label='SignUP')
        if submit_button:
            st.success("hello sigup successful")
        #Method 2
        form2 = st.form(key='form2',clear_on_submit=True)
        username = form2.text_input("Username:")
        jobtype = form2.selectbox("Job",["DA","DS"])
        submit_button2 = form2.form_submit_button("Login")

        if submit_button2:
            st.write(username.upper())


    else:
        st.subheader("About")

if __name__ == '__main__':
	main()
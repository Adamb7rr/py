import json
import streamlit as st


def login():
    print('login')

def register():
    col1, col2 = st.columns([1, 3])
    with col1:
        st.text_input("Enter Username")
    with col2:
        st.text_input("Enter Password")
    print('register')

def start_app():
    st.title("Bank System", text_alignment='center')
    col1, col2 = st.columns([1, 3])
    with col1:
        st.button("login", on_click=login)
    with col2:
        st.button("Register", on_click=register)

def main():
    start_app()

if __name__ == '__main__':
    main()
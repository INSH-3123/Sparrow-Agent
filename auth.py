from supabase_client import supabase
import streamlit as st


def check_session():
    session = supabase.auth.get_session()

    if session:
        st.session_state.logged_in = True
        st.session_state.user = session.user

def sign_up(email, password):
    response = supabase.auth.sign_up(
        {
            "email": email,
            "password": password,
        }
    )

    return response

def login(email, password):
    response = supabase.auth.sign_in_with_password(
        {
            "email": email,
            "password": password,
        }
    )

    st.session_state.logged_in = True
    st.session_state.user = response.user

    return response

def logout():
    supabase.auth.sign_out()

    st.session_state.logged_in = False
    st.session_state.user = None

    st.rerun()

from supabase_client import supabase
import streamlit as st

def sign_up(email, password):
    response = supabase.auth.sign_up(
        {
            "email": email,
            "password": password,
        }
    )
    return response
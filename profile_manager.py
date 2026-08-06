from supabase_client import supabase
import streamlit as st


def save_profile(
    qualification,
    experience_level,
    domain,
    target_role,
    career_goal,
):
    supabase.table("profiles").insert(
        {
            "user_id": st.session_state.user.id,
            "qualification": qualification,
            "experience_level": experience_level,
            "domain": domain,
            "target_role": target_role,
            "career_goal": career_goal,
            "onboarding_completed": True,
            "welcome_shown": False,
        }
    ).execute()

def get_profile():

    try:
        response = (
            supabase.table("profiles")
            .select("*")
            .eq("user_id", st.session_state.user.id)
            .single()
            .execute()
        )

        return response.data

    except Exception:
        return None

def mark_welcome_shown():
    supabase.table("profiles").update(
        {
            "welcome_shown": True
        }
    ).eq(
        "user_id",
        st.session_state.user.id
    ).execute()

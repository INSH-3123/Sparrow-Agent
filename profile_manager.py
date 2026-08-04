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

        print(response)
        st.write(response)

        return response.data

    except Exception:
        return None

def is_onboarding_complete():
    profile = get_profile()

    if profile:
        return profile["onboarding_completed"]

    return False
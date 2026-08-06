from supabase_client import supabase
import streamlit as st
import hashlib

def save_resume(
    resume_name,
    resume_url,
    resume_text,
):
    try:

        resume_hash = hashlib.sha256(
            resume_text.encode()
        ).hexdigest()

        # Check if this resume already exists for the current user
        existing = (
            supabase.table("resume_history")
            .select("id")
            .eq("user_id", st.session_state.user.id)
            .eq("resume_hash", resume_hash)
            .limit(1)
            .execute()
        )

        if existing.data:
            return existing.data[0]["id"]

        # Save as a new resume
        response = (
            supabase.table("resume_history")
            .insert(
                {
                    "user_id": st.session_state.user.id,
                    "resume_name": resume_name,
                    "resume_url": resume_url,
                    "resume_text": resume_text,
                    "resume_hash": resume_hash,
                }
            )
            .execute()
        )

        return response.data[0]["id"]

    except Exception as e:
        st.error(f"Failed to save resume: {e}")
        return None

def save_analysis(
    resume_id,
    detected_domain,
    confidence,
    resume_score,
    ats_score,
    career_readiness,
    best_role,
    analysis_data,
    report_url=None,
):

    try:

        response = (
            supabase.table("analysis_history")
            .insert(
                {
                    "resume_id": resume_id,
                    "detected_domain": detected_domain,
                    "confidence": confidence,
                    "resume_score": resume_score,
                    "ats_score": ats_score,
                    "career_readiness": career_readiness,
                    "best_role": best_role,
                    "analysis_data": analysis_data,
                    "report_url": report_url,
                }
            )
            .execute()
        )

        return response.data[0]["id"]

    except Exception as e:
        st.error(f"Failed to save analysis: {e}")
        return None

def get_resume_history():

    try:

        response = (
            supabase.table("resume_history")
            .select("*")
            .eq("user_id", st.session_state.user.id)
            .order("created_at", desc=True)
            .execute()
        )

        return response.data

    except Exception as e:

        st.error(f"Failed to load resume history: {e}")
        return []

def get_analysis_history(resume_id):

    try:

        response = (
            supabase.table("analysis_history")
            .select("*")
            .eq("resume_id", resume_id)
            .order("created_at", desc=True)
            .execute()
        )

        return response.data

    except Exception as e:

        st.error(f"Failed to load analysis history: {e}")
        return []

def upload_report(file_name, report):

    try:
        
        st.write("Current user:")
        st.write(supabase.auth.get_user())

        response = supabase.storage.from_("reports").upload(
            path=file_name,
            file=report.encode("utf-8"),
            file_options={
                "content-type": "text/plain",
                "upsert": "true",
            },
        )

        st.write(response)

        url = (
            supabase.storage
            .from_("reports")
            .get_public_url(file_name)
        )

        return url

    except Exception as e:

        st.error(f"Failed to upload report: {e}")
        return None
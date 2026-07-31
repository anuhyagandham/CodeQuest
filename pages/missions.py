import streamlit as st
from utils.helper import load_json


def _is_mission_completed(mission):
    if "completed" in mission:
        return bool(mission["completed"])

    if "progress" in mission:
        progress = mission["progress"]

        if isinstance(progress, bool):
            return progress

        if isinstance(progress, (int, float)):
            return progress >= 1

        if isinstance(progress, str):
            return progress.strip().lower() in {"done", "completed", "finished", "true", "1", "yes"}

    return False


def missions_page():
    st.title("🎯 Coding Missions")

    missions = load_json("data/missions.json")

    if not isinstance(missions, list):
        st.error("Mission data is invalid.")
        return

    total_xp = 0
    completed_count = 0

    for mission in missions:
        title = mission.get("title", "Untitled Mission")
        description = mission.get("description", "")
        xp = mission.get("xp", 0)

        st.subheader(title)
        st.write(description)

        if _is_mission_completed(mission):
            st.success("✅ Completed")
            completed_count += 1
            total_xp += xp
        else:
            st.warning("⏳ In Progress")

        st.write(f"⭐ XP Reward: {xp}")
        st.divider()

    st.subheader("📊 Mission Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Completed Missions", f"{completed_count}/{len(missions)}")

    with col2:
        st.metric("XP Earned", total_xp)
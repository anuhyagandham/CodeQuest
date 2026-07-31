import streamlit as st
from utils.helper import load_json


def achievements_page():

    user = load_json("data/user.json")
    if user["name"] == "Guest":
        st.warning("⚠ Create your profile first.")
        return

    st.title("🏅 Achievements")

    st.info("Unlock achievements by improving your coding journey!")

    st.markdown("---")

    achievements = []

    # GitHub
    if user["public_repos"] >= 1:
        achievements.append(("📦", "First GitHub Repository", "Created your first public repository."))

    if user["followers"] >= 5:
        achievements.append(("👥", "Community Builder", "Reached 5 GitHub followers."))

    # LeetCode
    if user["problemsSolved"] >= 10:
        achievements.append(("💻", "Problem Solver", "Solved 10+ LeetCode problems."))

    if user["problemsSolved"] >= 25:
        achievements.append(("🥉", "Coding Enthusiast", "Solved 25+ problems."))

    if user["problemsSolved"] >= 50:
        achievements.append(("🥈", "Advanced Coder", "Solved 50+ problems."))

    if user["problemsSolved"] >= 100:
        achievements.append(("🏆", "Elite Programmer", "Solved 100+ problems."))

    # XP
    if user["xp"] >= 500:
        achievements.append(("🔥", "XP Warrior", "Earned 500 XP."))

    if user["xp"] >= 1000:
        achievements.append(("💎", "XP Master", "Earned 1000 XP."))

    # Level
    if user["level"] >= 5:
        achievements.append(("⭐", "Level 5 Achiever", "Reached Level 5."))

    if user["level"] >= 10:
        achievements.append(("🌟", "Level 10 Hero", "Reached Level 10."))

    # Streak
    if user["streak"] >= 7:
        achievements.append(("🔥", "7-Day Streak", "Maintained a 7-day coding streak."))

    if user["streak"] >= 30:
        achievements.append(("🏅", "Consistency Champion", "Maintained a 30-day streak."))

    if achievements:

        cols = st.columns(2)

        for i, achievement in enumerate(achievements):

            with cols[i % 2]:

                st.success(f"{achievement[0]} **{achievement[1]}**")

                st.caption(achievement[2])

    else:

        st.warning("No achievements unlocked yet.")

    st.markdown("---")

    st.metric("🏅 Total Achievements", len(achievements))

    st.caption("🎮 Keep coding to unlock more achievements!")
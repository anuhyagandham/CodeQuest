import streamlit as st
from utils.helper import load_json


def skill_tree_page():

    user = load_json("data/user.json")

    if user["name"] == "Guest":
        st.warning("Please create your profile first.")
        return

    xp = user.get("xp", 0)
    level = user.get("level", 1)
    rank = user.get("rank", "Beginner")

    # Skills based on XP
    python_skill = min(int(xp / 8), 100)
    sql_skill = min(int(xp / 10), 100)
    problem_skill = min(int(xp / 7), 100)
    git_skill = min(int(xp / 12), 100)

    st.title("Skill Tree")
    st.write("Track your learning progress based on your coding activity.")

    st.markdown("---")

    c1, c2, c3 = st.columns(3)

    c1.metric("Current Level", level)
    c2.metric("Current XP", xp)
    c3.metric("Current Rank", rank)

    st.markdown("---")

    st.subheader("Skill Progress")

    st.write("Python")
    st.progress(python_skill / 100)
    st.caption(f"{python_skill}%")

    st.write("SQL")
    st.progress(sql_skill / 100)
    st.caption(f"{sql_skill}%")

    st.write("Problem Solving")
    st.progress(problem_skill / 100)
    st.caption(f"{problem_skill}%")

    st.write("Git")
    st.progress(git_skill / 100)
    st.caption(f"{git_skill}%")

    st.markdown("---")

    st.subheader("Unlocked Skills")

    unlocked = []

    if python_skill >= 20:
        unlocked.append("Python Basics")

    if python_skill >= 40:
        unlocked.append("Functions")

    if python_skill >= 60:
        unlocked.append("Object Oriented Programming")

    if sql_skill >= 20:
        unlocked.append("SQL Queries")

    if sql_skill >= 40:
        unlocked.append("Joins")

    if problem_skill >= 50:
        unlocked.append("Problem Solving")

    if git_skill >= 30:
        unlocked.append("Git Version Control")

    if len(unlocked) == 0:
        st.info("No skills unlocked yet.")

    for skill in unlocked:
        st.success(skill)

    st.markdown("---")

    st.subheader("Upcoming Skills")

    locked = []

    if python_skill < 80:
        locked.append("APIs")

    if python_skill < 90:
        locked.append("NumPy")

    if python_skill < 95:
        locked.append("Pandas")

    if python_skill < 100:
        locked.append("Streamlit")

    if problem_skill < 100:
        locked.append("Advanced DSA")

    for skill in locked:
        st.write("🔒", skill)

    st.markdown("---")

    next_level_xp = level * 100
    remaining = max(next_level_xp - xp, 0)

    st.subheader("Next Level")

    st.write(f"You need **{remaining} XP** to reach **Level {level + 1}**.")

    st.progress(min(xp / next_level_xp, 1.0))

    st.markdown("---")

    st.info(
        "Skills improve automatically as you solve more coding problems and gain XP."
    )
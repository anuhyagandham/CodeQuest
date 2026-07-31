import streamlit as st
from utils.helper import load_json


def profile_page():

    user = load_json("data/user.json")

    if user["name"] == "Guest":
        st.warning("Please create your profile from Home.")
        return

    st.title("Developer Profile")

    st.markdown("---")

    col1, col2 = st.columns([1, 3])

    with col1:
        st.image(
            f"https://api.dicebear.com/7.x/initials/png?seed={user['name']}",
            width=170
        )

    with col2:
        st.header(user["name"])
        st.write("Python Developer")
        st.write(f"Current Rank : **{user['rank']}**")
        st.write(f"Level : **{user['level']}**")
        st.write(f"XP : **{user['xp']}**")

    st.markdown("---")

    st.subheader("Platform Accounts")

    c1, c2 = st.columns(2)

    with c1:
        st.write("**LeetCode Username**")
        st.code(user["leetcode"])

    with c2:
        st.write("**GitHub Username**")
        st.code(user["github"])

    st.markdown("---")

    st.subheader("Coding Statistics")

    c1, c2, c3 = st.columns(3)

    c1.metric("Problems Solved", user["problemsSolved"])
    c2.metric("Repositories", user["public_repos"])
    c3.metric("Followers", user["followers"])

    st.markdown("---")

    st.subheader("About")

    st.info(
        f"""
{user['name']} is actively improving programming skills by solving coding
problems on LeetCode and building projects using GitHub.

Current focus is improving problem-solving ability and maintaining coding consistency.
"""
    )

    st.markdown("---")

    st.subheader("Recent Activity")

    st.write("• Logged into CodeQuest")
    st.write(f"• Solved {user['problemsSolved']} coding problems")
    st.write(f"• Published {user['public_repos']} GitHub repositories")
    st.write(f"• Current coding streak: {user['streak']} days")
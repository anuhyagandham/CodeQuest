import streamlit as st
from utils.helper import load_json, save_json


def settings_page():

    user = load_json("data/user.json")

    if user["name"] == "Guest":
        st.warning("Please create your profile from Home.")
        return

    st.title("Settings")

    st.markdown("---")

    st.subheader("Current User")

    st.write(f"Name : {user['name']}")
    st.write(f"Level : {user['level']}")
    st.write(f"XP : {user['xp']}")

    st.markdown("---")

    if st.button("Logout"):

        guest = {
            "name": "Guest",
            "leetcode": "",
            "github": "",
            "xp": 0,
            "level": 1,
            "rank": "Beginner",
            "streak": 0,
            "avatar": "Rookie",
            "problemsSolved": 0,
            "easySolved": 0,
            "mediumSolved": 0,
            "hardSolved": 0,
            "leetcodeRanking": 0,
            "public_repos": 0,
            "followers": 0,
            "following": 0
        }

        save_json("data/user.json", guest)

        st.success("Logged out successfully.")

        st.rerun()
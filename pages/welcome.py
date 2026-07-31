import streamlit as st
import os
from services.tracker import get_github_data, get_leetcode_data
from utils.helper import load_json, save_json, update_leaderboard


def welcome_page():

    # ==========================
    # Load Current User
    # ==========================

    user = load_json("data/user.json")

    # ==========================
    # Logged In User
    # ==========================

    if user["name"] != "Guest":

        st.title("CodeQuest")

        st.subheader(f"Welcome back, {user['name']}")

        st.markdown("---")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("XP", user["xp"])
        c2.metric("Level", user["level"])
        c3.metric("Problems Solved", user["problemsSolved"])
        c4.metric("Repositories", user["public_repos"])

        st.markdown("---")

        st.subheader("Today's Progress")

        next_level_xp = user["level"] * 100

        progress = min(user["xp"] / next_level_xp, 1.0)

        st.progress(progress)

        st.write(f"Current XP : {user['xp']} / {next_level_xp}")

        st.markdown("---")

        left, right = st.columns(2)

        with left:

            st.subheader("LeetCode Summary")

            st.write(f"Easy : {user['easySolved']}")
            st.write(f"Medium : {user['mediumSolved']}")
            st.write(f"Hard : {user['hardSolved']}")
            st.write(f"Global Rank : {user['leetcodeRanking']:,}")

        with right:

            st.subheader("GitHub Summary")

            st.write(f"Repositories : {user['public_repos']}")
            st.write(f"Followers : {user['followers']}")
            st.write(f"Following : {user['following']}")

        st.markdown("---")

        st.success(f"Current Rank : {user['rank']}")

        return

    # ==========================
    # Guest Screen
    # ==========================

    st.title("Welcome to CodeQuest")

    st.write("Create your coding profile to start your coding journey.")

    st.markdown("---")

    name = st.text_input("Your Name")

    leetcode = st.text_input("LeetCode Username")

    github = st.text_input("GitHub Username")

    if st.button("Create Profile"):

        if name == "" or leetcode == "" or github == "":
            st.error("Please fill all the fields.")
            return

        github_data = get_github_data(github)

        if github_data is None:
            st.error("Invalid GitHub Username")
            return

        leetcode_data = get_leetcode_data(leetcode)

        if leetcode_data is None:
            st.error("Invalid LeetCode Username")
            return

        xp = (
            leetcode_data["totalSolved"] * 20
            + github_data["public_repos"] * 10
        )

        level = max(1, xp // 100 + 1)

        if xp >= 2000:
            rank = "Legend"

        elif xp >= 1500:
            rank = "Master"

        elif xp >= 1000:
            rank = "Expert"

        elif xp >= 500:
            rank = "Intermediate"

        else:
            rank = "Beginner"

        user = {

            "name": name,
            "leetcode": leetcode,
            "github": github,

            "xp": xp,
            "level": level,
            "rank": rank,

            "streak": 0,
            "avatar": "Rookie",

            "problemsSolved": leetcode_data["totalSolved"],
            "easySolved": leetcode_data["easySolved"],
            "mediumSolved": leetcode_data["mediumSolved"],
            "hardSolved": leetcode_data["hardSolved"],
            "leetcodeRanking": leetcode_data["ranking"],

            "public_repos": github_data["public_repos"],
            "followers": github_data["followers"],
            "following": github_data["following"]

        }

        os.makedirs("data", exist_ok=True)

        # Save current user
        save_json("data/user.json", user)

        # Update leaderboard
        update_leaderboard(user)

        st.success("Profile Created Successfully!")

        st.rerun()
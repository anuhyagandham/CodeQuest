import streamlit as st
import pandas as pd
from utils.helper import load_json


def leaderboard_page():

    user = load_json("data/user.json")

    if user["name"] == "Guest":
        st.warning("Please create your profile from Home.")
        return

    leaderboard = load_json("data/leaderboard.json")

    st.title("Leaderboard")

    st.write("Top performers in CodeQuest")

    st.markdown("---")

    if len(leaderboard) == 0:
        st.info("No users available.")
        return

    # Sort by XP
    leaderboard = sorted(
        leaderboard,
        key=lambda x: x["xp"],
        reverse=True
    )

    table = []

    for index, player in enumerate(leaderboard, start=1):

        table.append({

            "Rank": index,

            "Name": player["name"],

            "Level": player["level"],

            "XP": player["xp"],

            "Problems Solved": player["problemsSolved"],

            "Rank Title": player["rank"]

        })

    df = pd.DataFrame(table)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    st.subheader("Top Performer")

    top = leaderboard[0]

    c1, c2, c3 = st.columns(3)

    c1.metric("Name", top["name"])
    c2.metric("XP", top["xp"])
    c3.metric("Level", top["level"])

    st.markdown("---")

    st.caption(
        "Leaderboard updates automatically whenever a user creates a profile."
    )
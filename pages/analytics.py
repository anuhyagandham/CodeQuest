import streamlit as st
import plotly.express as px
from utils.helper import load_json


def analytics_page():

    st.title("Analytics Dashboard")
    st.write("Track your coding progress using your actual CodeQuest profile data.")

    try:
        user = load_json("data/user.json")
    except:
        st.warning("No user data found.")
        return

    st.markdown("---")

    # =========================
    # Overall Summary
    # =========================

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("XP", user["xp"])
    c2.metric("Level", user["level"])
    c3.metric("Problems Solved", user["problemsSolved"])
    c4.metric("Rank", user["rank"])

    st.markdown("---")

    # =========================
    # LeetCode Progress
    # =========================

    st.subheader("LeetCode Progress")

    lc_data = {
        "Difficulty": ["Easy", "Medium", "Hard"],
        "Solved": [
            user["easySolved"],
            user["mediumSolved"],
            user["hardSolved"]
        ]
    }

    fig = px.bar(
        lc_data,
        x="Difficulty",
        y="Solved",
        text="Solved",
        color="Difficulty",
        color_discrete_sequence=[
            "#4CAF50",
            "#FFC107",
            "#F44336"
        ]
    )

    fig.update_layout(
        height=420,
        showlegend=False,
        plot_bgcolor="white",
        paper_bgcolor="white",
        xaxis_title="",
        yaxis_title="Problems Solved"
    )

    fig.update_traces(textposition="outside")

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # =========================
    # GitHub Statistics
    # =========================

    st.subheader("GitHub Statistics")

    github_data = {
        "Category": [
            "Repositories",
            "Followers",
            "Following"
        ],
        "Count": [
            user["public_repos"],
            user["followers"],
            user["following"]
        ]
    }

    # If all values are zero, don't draw an empty chart.
    if sum(github_data["Count"]) == 0:

        st.info("No GitHub statistics available yet.")

    else:

        fig2 = px.bar(
            github_data,
            x="Category",
            y="Count",
            text="Count",
            color="Category",
            color_discrete_sequence=[
                "#2563EB",
                "#7C3AED",
                "#10B981"
            ]
        )

        fig2.update_layout(
            height=420,
            showlegend=False,
            plot_bgcolor="white",
            paper_bgcolor="white",
            xaxis_title="",
            yaxis_title="Count"
        )

        fig2.update_traces(textposition="outside")

        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")

    # =========================
    # Coding Progress
    # =========================

    st.subheader("Overall Coding Progress")

    next_level = user["level"] * 100

    progress = min(user["xp"] / next_level, 1.0)

    st.progress(progress)

    st.write(
        f"Current XP : {user['xp']} / {next_level}"
    )

    st.markdown("---")

    # =========================
    # Performance Insights
    # =========================

    st.subheader("Performance Insights")

    st.success(f"Current Rank : {user['rank']}")

    st.write("• Keep solving coding problems consistently.")

    st.write("• Increase GitHub repositories to earn more XP.")

    st.write("• Solve more Medium and Hard problems.")

    st.write("• Maintain your coding streak to level up faster.")
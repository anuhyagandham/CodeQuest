import streamlit as st
from utils.helper import load_json
from utils.ui import stat_card, section, activity


def dashboard_page():

    # ==========================
    # LOAD USER
    # ==========================

    user = load_json("data/user.json")

    if user["name"] == "Guest":
        st.warning("⚠ Please create your profile from the Welcome page.")
        return

    missions = load_json("data/missions.json")

    # ==========================
    # HERO SECTION
    # ==========================

    st.title("🎮 CodeQuest")

    st.caption("Gamified Coding Journey")

    st.markdown(
        f"""
        ## Welcome back, **{user['name']}** 👋

        _"Every problem you solve today makes you stronger tomorrow."_ 🚀
        """
    )

    st.markdown("---")

    # ==========================
    # PLAYER STATS
    # ==========================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        stat_card(
            "Total XP",
            user["xp"],
            "⭐"
        )

    with c2:
        stat_card(
            "Current Level",
            user["level"],
            "🏆"
        )

    with c3:
        stat_card(
            "Current Rank",
            user["rank"],
            "🥇"
        )

    with c4:
        stat_card(
            "Coding Streak",
            f"{user['streak']} Days",
            "🔥"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ==========================
    # TODAY'S MISSION
    # ==========================

    section("🎯 Today's Mission")

    problems = user["problemsSolved"]

    if problems < 20:

        mission = "Solve 2 Easy Problems"

        reward = 50

        progress = problems / 20

    elif problems < 50:

        mission = "Solve 1 Medium Problem"

        reward = 100

        progress = problems / 50

    else:

        mission = "Solve 1 Hard Problem"

        reward = 150

        progress = min(problems / 100, 1.0)

    st.info(f"🎯 **{mission}**")

    st.progress(progress)

    st.success(f"🏆 Reward : +{reward} XP")

    st.markdown("---")

    # ==========================
    # QUICK OVERVIEW
    # ==========================

    section("⚡ Quick Overview")

    q1, q2 = st.columns(2)

    with q1:

        st.metric(
            "💻 Problems Solved",
            user["problemsSolved"]
        )

        st.metric(
            "📦 GitHub Repositories",
            user["public_repos"]
        )

    with q2:

        st.metric(
            "👥 Followers",
            user["followers"]
        )

        st.metric(
            "🌍 Global Rank",
            f"{user['leetcodeRanking']:,}"
        )

    st.markdown("---")
        # ==========================
    # XP PROGRESS
    # ==========================

    section("📈 XP Progress")

    current_xp = user["xp"]

    next_level_xp = user["level"] * 100

    progress = min(current_xp / next_level_xp, 1.0)

    st.progress(progress)

    st.write(f"**{current_xp} / {next_level_xp} XP**")

    st.markdown("---")

    # ==========================
    # DAILY MISSIONS
    # ==========================

    section("📋 Active Missions")

    for mission in missions:

        st.write(f"### 🎯 {mission['title']}")

        mission_progress = mission["progress"] / mission["target"]

        st.progress(mission_progress)

        st.caption(
            f"{mission['progress']} / {mission['target']} Completed"
        )

        st.success(f"Reward : {mission['reward']}")

        st.markdown("")

    st.markdown("---")

    # ==========================
    # RECENT ACTIVITY
    # ==========================

    section("📅 Recent Activity")

    activity("GitHub account connected successfully")

    activity("LeetCode profile synchronized")

    activity("Player profile loaded")

    activity("Ready for today's coding challenge")

    st.markdown("---")

    # ==========================
    # PLAYER INFO
    # ==========================

    section("🎮 Player")

    left, right = st.columns(2)

    with left:

        st.success(f"🏅 Badge : {user['avatar']}")

    with right:

        st.info(f"🥇 Rank : {user['rank']}")

    st.markdown("---")

    st.caption(
        "🎮 CodeQuest • Gamified Coding Journey"
    )
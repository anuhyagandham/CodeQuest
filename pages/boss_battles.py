import streamlit as st
from utils.helper import load_json


def boss_page():

    user = load_json("data/user.json")

    if user["name"] == "Guest":
        st.warning("Please create your profile from the Home page.")
        return

    solved = user.get("problemsSolved", 0)
    xp = user.get("xp", 0)
    level = user.get("level", 1)
    rank = user.get("rank", "Beginner")

    target = 50
    remaining = max(target - solved, 0)

    st.title("Weekly Boss Battle")
    st.write("Complete the weekly coding challenge to unlock the next stage.")

    st.markdown("---")

    left, right = st.columns([2,1])

    with left:

        st.subheader("Current Boss")

        st.info("""
Boss Name : Python Titan

Difficulty : Medium

Mission :
Solve 50 coding problems before completing this stage.
""")

    with right:

        st.metric("Current Level", level)
        st.metric("Current Rank", rank)

    st.markdown("---")

    st.subheader("Battle Progress")

    c1, c2, c3 = st.columns(3)

    c1.metric("Problems Solved", solved)
    c2.metric("Target", target)
    c3.metric("Remaining", remaining)

    completion = int((solved / target) * 100)

    if completion > 100:
        completion = 100

    st.write(f"Completion : {completion}%")
    st.progress(completion / 100)

    st.markdown("---")

    st.subheader("Rewards")

    r1, r2, r3 = st.columns(3)

    r1.metric("Bonus XP", "500")
    r2.metric("Special Badge", "Boss Slayer")

    if solved >= target:
        r3.metric("Status", "Completed")
        st.success("Boss defeated successfully. Next challenge unlocked.")
    else:
        r3.metric("Status", "Active")
        st.warning(f"{remaining} more problems required to defeat this boss.")

    st.markdown("---")

    st.subheader("Performance Summary")

    a, b, c = st.columns(3)

    a.metric("Current XP", xp)
    b.metric("Level", level)
    c.metric("Coding Rank", rank)

    st.markdown("---")

    st.subheader("Why this Boss Battle?")

    st.write("""
This weekly challenge encourages consistent coding practice.

• Solve coding problems regularly.

• Improve problem-solving ability.

• Earn bonus XP after completion.

• Unlock higher-level coding challenges.

• Increase your overall rank in CodeQuest.
""")
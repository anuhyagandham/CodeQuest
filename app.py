import streamlit as st
from config import APP_NAME
from utils.helper import load_json

# ===============================
# Load CSS
# ===============================

def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ===============================
# Page Config
# ===============================

st.set_page_config(
    page_title=APP_NAME,
    page_icon="💻",
    layout="wide"
)

# ===============================
# Load User
# ===============================

try:
    user = load_json("data/user.json")
except:
    user = {
        "name": "Guest",
        "level": 1,
        "xp": 0,
        "rank": "Beginner"
    }

# ===============================
# Sidebar
# ===============================

st.sidebar.title("CodeQuest")
st.sidebar.caption("Gamified Coding Journey")

st.sidebar.markdown("---")

if user["name"] != "Guest":

    st.sidebar.subheader(user["name"])

    st.sidebar.write(f"Level : {user['level']}")
    st.sidebar.write(f"XP : {user['xp']}")
    st.sidebar.write(f"Rank : {user['rank']}")

else:

    st.sidebar.info("Guest User")

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Profile",
        "Missions",
        "Boss Battle",
        "Skill Tree",
        "Leaderboard",
        "Analytics",
        "Settings"
    ]
)

# ===============================
# Import Pages
# ===============================

from pages.welcome import welcome_page
from pages.profile import profile_page
from pages.missions import missions_page
from pages.boss_battles import boss_page
from pages.skill_tree import skill_tree_page
from pages.leaderboard import leaderboard_page
from pages.analytics import analytics_page
from pages.settings import settings_page

# ===============================
# Page Routing
# ===============================

if page == "Home":
    welcome_page()

elif page == "Profile":
    profile_page()

elif page == "Missions":
    missions_page()

elif page == "Boss Battle":
    boss_page()

elif page == "Skill Tree":
    skill_tree_page()

elif page == "Leaderboard":
    leaderboard_page()

elif page == "Analytics":
    analytics_page()

elif page == "Settings":
    settings_page()
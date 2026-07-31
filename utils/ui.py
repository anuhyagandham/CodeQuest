import streamlit as st


def stat_card(title, value):
    st.markdown(
        f"""
        <div class="card">
            <h5 style="margin:0;color:#6b7280;">
                {title}
            </h5>

            <h2 style="margin-top:10px;color:#111827;">
                {value}
            </h2>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section(title):
    st.markdown(f"## {title}")


def activity(text):
    st.success(text)
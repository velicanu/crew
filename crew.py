import os

import numpy as np
import streamlit as st


def get_goals(ngoals, nplayers):
    filter_ = lambda x: "green" not in x if nplayers < 4 else lambda x: x  # noqa: E731
    goals = [card for card in filter(filter_, os.listdir("goals"))]
    st.session_state.goals = np.random.permutation(goals)[:ngoals]


st.markdown("# Crew Goal Picker")
st.markdown("Pick settings to randomize goals")
col1, col2, col3 = st.columns(3)
with col1:
    ngoals = st.selectbox(label="Goals", options=(1, 2, 3, 4, 5, 6, 7, 8, 9), index=3)
with col2:
    nplayers = st.selectbox(label="Players", options=(3, 4, 5), index=1)
with col3:
    pick = st.button("Pick", on_click=get_goals, args=(ngoals, nplayers))

if len(st.session_state.get("goals", [])) > 0:
    cols = st.columns(4)
    for idx, card in enumerate(st.session_state.goals):
        with cols[idx % 4] as col:
            st.image(f"goals/{card}")

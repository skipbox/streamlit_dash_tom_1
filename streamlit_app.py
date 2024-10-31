import streamlit as st
import streamlit.components.v1 as components
import time

# Sidebar with accordion
with st.sidebar:
    with st.expander("Options", expanded=True):
        button_1 = st.button("App 1", key="button_1")
        button_2 = st.button("App 2", key="button_2")
        button_3 = st.button("App 3", key="button_3")

# Display different groups of buttons based on clicked button
image_style = "display: block; margin: 10px auto; width: 200px; height: 200px; object-fit: cover; border: solid 2px;"

if button_1:
    st.sidebar.write("Group 1")
    st.sidebar.button("Group 1 - Button A")
    st.sidebar.button("Group 1 - Button B")
    st.write("App 1")
    st.markdown(f"<img src='https://i.imgur.com/DM1YhSh_d.webp?maxwidth=520&shape=thumb&fidelity=high' style='{image_style}' />", unsafe_allow_html=True)
elif button_2:
    st.sidebar.write("Group 2")
    st.sidebar.button("Group 2 - Button C")
    st.sidebar.button("Group 2 - Button D")
    st.write("App 2")
    st.markdown(f"<img src='https://i.imgur.com/F9LQwyA_d.webp?maxwidth=520&shape=thumb&fidelity=high' style='{image_style}' />", unsafe_allow_html=True)
elif button_3:
    st.sidebar.write("Group 3")
    st.sidebar.button("Group 3 - Button E")
    st.sidebar.button("Group 3 - Button F")
    st.write("App 3")
    st.markdown(f"<img src='https://i.imgur.com/2ueW1arb.jpg' style='{image_style}' />", unsafe_allow_html=True)

import streamlit as st
import time

# Sidebar with accordion
with st.sidebar:
    with st.expander("Options", expanded=True):
        button_1 = st.button("App 1", key="button_1")
        button_2 = st.button("App 2", key="button_2")
        button_3 = st.button("App 3", key="button_3")

# Display different groups of buttons based on clicked button
if button_1:
    st.sidebar.write("Group 1")
    st.sidebar.button("Group 1 - Button A")
    st.sidebar.button("Group 1 - Button B")
    st.write("App 1")
    # Display 3 images side by side using columns
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://i.imgur.com/DM1YhSh_d.webp?maxwidth=520&shape=thumb&fidelity=high", width=200)
        st.write("Lorem ipsum dolor sit amet.")
        st.text_area("Text Area 1", "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", height=100)
    with col2:
        st.image("https://i.imgur.com/DM1YhSh_d.webp?maxwidth=520&shape=thumb&fidelity=high", width=200)
        st.write("Lorem ipsum dolor sit amet.")
        st.text_area("Text Area 2", "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", height=100)
    with col3:
        st.image("https://i.imgur.com/DM1YhSh_d.webp?maxwidth=520&shape=thumb&fidelity=high", width=200)
        st.write("Lorem ipsum dolor sit amet.")
        st.text_area("Text Area 3", "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", height=100)
elif button_2:
    st.sidebar.write("Group 2")
    st.sidebar.button("Group 2 - Button C")
    st.sidebar.button("Group 2 - Button D")
    st.write("App 2")
    st.image("https://i.imgur.com/DM1YhSh_d.webp?maxwidth=520&shape=thumb&fidelity=high", width=200)
elif button_3:
    st.sidebar.write("Group 3")
    st.sidebar.button("Group 3 - Button E")
    st.sidebar.button("Group 3 - Button F")
    st.write("App 3")
    st.image("https://i.imgur.com/DM1YhSh_d.webp?maxwidth=520&shape=thumb&fidelity=high", width=200)

import streamlit as st

st.set_page_config(page_title="Friendship Check 😂")

st.title("😂 FRIENDSHIP VERIFICATION")
st.write("Complete these two important questions to enter!")

if "step" not in st.session_state:
    st.session_state.step = 1

if st.session_state.step == 1:
    st.subheader("Step 1")
    st.write("I ACCEPT THAT I AM LESBIAN 🏳️‍🌈")

    if st.button("ACCEPT 😂"):
        st.session_state.step = 2
        st.rerun()

elif st.session_state.step == 2:
    st.subheader("Step 2")
    st.write("I ACCEPT THAT I AM NOT STRAIGHT 😂")

    if st.button("ACCEPT 🤣"):
        st.session_state.step = 3
        st.rerun()

elif st.session_state.step == 3:
    st.balloons()
    st.title("CONGRATULATIONS! 🤣")
    st.header("EAM UNDHI LEE PANDUKO INGA!")
    st.write("You have successfully completed the friendship test!")
    st.error("YOU HAVE BEEN PRANKED! 😂")
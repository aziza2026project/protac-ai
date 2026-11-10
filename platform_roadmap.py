import streamlit as st
def render():
    st.title("Platform Roadmap")
    st.write("The interface is being prepared first. Scientific datasets and engines can be connected later without redesigning the whole app.")
    stages=[("1. Interface & workflows","Current phase","Build service pages, forms, navigation, portal layouts, and clear workflow states."),("2. Scientific data","Later","Import spreadsheets safely, preserve originals, normalize records, and track provenance."),("3. Scientific engines","Later","Select and validate docking, structure visualization, chemistry, linker, and prediction tools."),("4. Accounts & requests","Later","Configure authentication, database, secure file storage, notifications, and role-based access."),("5. Payments & deployment","Later","Confirm payment provider eligibility, enforce service access server-side, test, and deploy.")]
    for title,status,detail in stages:
        with st.container(border=True): st.markdown(f"**{title}** · `{status}`"); st.write(detail)
    st.warning("This prototype does not yet store submitted requests, authenticate users, process payments, or run unconnected scientific calculations. Do not upload confidential or sensitive files to this demo.")

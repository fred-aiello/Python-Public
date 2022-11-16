# Contents of ~/my_app/pages/page_3.py
import streamlit as st

st.set_page_config(
    page_title="Hello Fred",
    page_icon="👋",
    menu_items={
    'Get Help':'https://www.yahoo.fr',
   'Report a bug': 'https://www.boursotama.com',
}
)


st.markdown("# Page 4 🎉")
st.sidebar.markdown("# Page 4 🎉")

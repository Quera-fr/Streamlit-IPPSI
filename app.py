import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = 'Scraping BDM',
    page_icon='🐯',
    layout='centered'
)
#Load Data
df = pd.read_json('data.json').T

# Title
st.title('My First App Streamlit - V1')
# Text
st.write('Ceci est une zone de text')

# Markdown
st.markdown(
"""
# Titre 1

## Titre 2

`print("hello world")`         
""")

# Checkbox
if st.checkbox('Show information'):
    st.write(df)

# SelectBox
user_selct = st.selectbox('Select your article', range(15))

col1, col2 = st.columns(2)

with col1:
    # Show Image
    st.image(df.iloc[user_selct].image)
with col2:
    st.write(df.iloc[user_selct].title)


# Formulaire
with st.form("First Form"):
    user_input = st.text_input("Tap your text")     # Input
    
    if st.form_submit_button('Send'):               # Submit Button Form
        st.write(user_input)
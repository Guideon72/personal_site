import streamlit as st
import pandas

st.set_page_config(page_title="Title for my page", layout="wide")

col1, col2 = st.columns(2)

st.markdown(
    """ <style> .font {
font-size:2em ; font-family: 'Ariel'; color: #366222;}
</style> """,
    unsafe_allow_html=True,
)


def display_centered_text(text: str, container=None):
    if container is not None:
        container.markdown(
            f"<div style='text-align: center;'>{text}</div>", unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div style='text-align: center;'>{text}</div>", unsafe_allow_html=True
        )


with col1:
    st.image("./images/photo.png", width=400)

with col2:
    st.title("My name goes here, eventually")
    content = """Write something about 
    yourself here"""
    st.info(content)

with st.sidebar:
    st.text("This is my sidebar; there is only one like it.")

# app_content = (
#     """Here are a few of the web apps built using Python during the video course"""
# )
app_content = st.markdown(
    '<p class="font">These are just a few of the web apps we have built using Python and Streamlit.</p>',
    unsafe_allow_html=True,
)
st.write(
    "_____________________________________________________________________________________________"
)

df = pandas.read_csv("data/data.csv", sep=";")

col3, empty_col, col4 = st.columns([1.5, 0.1, 1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=200)
        st.write(f'[Source Code: ]({row["url"]})')

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=200)
        st.write(f'[Source Code: ]({row["url"]})')

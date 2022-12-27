import streamlit as st
import mail_client as mc

st.set_page_config(page_title="Contact", layout="wide")

if "content" not in st.session_state:
    st.session_state["content"] = ""


def send_mail():
    contact_user = st.session_state["address"]
    body = st.session_state["content"]
    # If you fix the indentation here, the email will print everything in the subject line
    message = f"""\
Subject: New Portfolio message

From: {contact_user}
{body}
"""
    mc.esend(message)
    st.info("Your email was sent")


st.header("Contact Us")

with st.form(key="email_form", clear_on_submit=True):
    st.text_input(
        label="Email Address",
        max_chars=32,
        key="address",
    )
    st.text_area("Message", max_chars=500, key="content")

    st.form_submit_button("Send Email", on_click=send_mail)

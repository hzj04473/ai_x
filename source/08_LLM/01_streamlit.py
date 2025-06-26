# ctrl+shift+p : 인터프리터 선택
from turtle import onclick
import streamlit as st

st.set_page_config(
    page_title="나x의 첫 streamlit 프로그램",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("나의 첫 streamlit 웹")
st.subheader("웹 앱을 만들기 위한 강력한 라이브러리 : streamlit")
st.info("text 출력")

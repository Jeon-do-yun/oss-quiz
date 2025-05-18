import streamlit as st

st.set_page_config(page_title="퀴즈 앱", page_icon="❓")
st.title("간단한 퀴즈 앱")
st.write("객관식 1문제, 주관식 1문제에 도전해보세요!")

# 객관식 문제
st.header("문제 1 (객관식)")
q1 = st.radio("파이썬에서 리스트의 길이를 구하는 함수는?", ["count()", "length()", "len()", "size()"])

if st.button("문제 1 제출"):
    if q1 == "len()":
        st.success("정답입니다! 🎉")
    else:
        st.error("오답입니다. 정답은 len()입니다.")

# 주관식 문제
st.header("문제 2 (주관식)")
q2 = st.text_input("파이썬에서 조건문을 작성할 때 사용하는 키워드는 무엇인가요?")

if st.button("문제 2 제출"):
    if q2.strip().lower() == "if":
        st.success("정답입니다! 🎉")
    else:
        st.error("오답입니다. 정답은 'if'입니다.")
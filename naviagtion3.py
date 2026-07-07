# naviagtion3.py
import streamlit as st

# 현재 페이지 확인
current_page = st.query_params.get('page', ['home'])

# 페이지에 따라 올바른 콘텐츠 표시
if current_page == 'home':
    st.title('Home Page')
elif current_page == 'contact':
    st.title('Contact Page')

# 하위 URL 간 이동을 위한 링크 추가
st.sidebar.title('Pages')
if st.sidebar.button('Home'):
    st.query_params['page'] = 'home'
    st.rerun()
if st.sidebar.button('Contact'):
    st.query_params['page'] = 'contact'
    st.rerun()
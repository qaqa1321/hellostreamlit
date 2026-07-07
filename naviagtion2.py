# naviagtion2.py
import streamlit as st

pages = {
    '🏠 Home': [
        st.Page('pages/home.py', title='Home')
    ],
    '📞 Contact us': [
        st.Page('contact/message.py', title='Message'),
        st.Page('contact/address.py', title='Address'),
    ],
}

pg = st.navigation(pages)
pg.run()
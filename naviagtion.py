# naviagtion.py
import streamlit as st

pg = st.navigation([st.Page('pages/home.py', title='🏠 Home'),
                    st.Page('pages/contact.py', title='📞 Contact us')])
pg.run()
import streamlit as st

st.title("Streamlit Basics")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is a simple text")
st.write("This is a write dimension")

st.markdown("[Streamlit](https://www.streamlit.io)")
st.markdown("https://www.streamlit.io")

html_page = """
<div style="background-color:orange; padding:50px">
<p style="color:white; font-size:50px">Enjoy Streamlit!</p>
</div>
"""
st.markdown(html_page, unsafe_allow_html=True)

st.success("Success!")
st.info("Information")
st.warning("This is a warning!")
st.error("This is an error!")

from PIL import Image

# img = Image.open("hello.jpeg")
# st.image(img, width=300, caption="Hello Logo")

st.image('https://youtu.be/UkFLk0-xf58?si=hgcFbkIkMqPYlN0y')

# video_file = open("SampleVideo_1280x720_1mb.mp4","rb")
# video_bytes = video_file.read()
# st.video(video_bytes)

st.video("https://www.youtube.com/watch?v=UkFLk0-xf58")

# audio_file = open("sample1.mp3", "rb")
# audio_bytes = audio_file.read()
# st.audio(audio_bytes, format="audio/mp3")

st.button("Play1")

if st.button("Play2"):
      st.text("Hello world!")
      
if st.checkbox("Checkbox"):
      st.text("Checkbox selected")
      
radio_but = st.radio("Your Selection", ["A", "B"])
if radio_but == "A":
      st.info("You selected A")
else:
      st.info("You selected B")
      
city = st.selectbox("Your City", ["Napoli", "Palermo", "Catania"])

occupation = st.multiselect("Your Occupation", 
	["Programmer", "Data Scientist", "IT Consultant", "DBA"])

name = st.text_input("Your Name", "Write something…")
st.text(name)

age = st.number_input("Input a number")

message = st.text_area("Your Message", "Write something...")

select_val = st.slider("Select a Value", 1, 10)

if st.button("Balloons"):
      st.balloons()

import datetime
import time

today = st.date_input("Today is",datetime.datetime.now())
hour = st.time_input("The time is",datetime.time(12,30))

data = {"name":"John","surname":"Wick"}

st.json(data)
st.code("import pandas as pd")

import time

my_bar = st.progress(0)

for value in range(100):
      time.sleep(0.05)
      my_bar.progress(value+1)
      
with st.spinner("Please wait..."):
      time.sleep(3)
      
st.success("Done!")      

import pandas as pd

st.header("Dataframes and Tables")
df = pd.read_csv("csv/auto.csv")
st.dataframe(df.head(10))

st.table(df.head(10)) 

st.area_chart(df[["mpg","cylinders"]])

st.bar_chart(df[["mpg","cylinders"]].head(20))

st.line_chart(df[["mpg","cylinders"]].head(20))

import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots()
corr_plot = sns.heatmap(df[["mpg","cylinders", "displacement"]].corr(), annot= True)
st.pyplot(fig)
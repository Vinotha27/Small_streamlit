#import Packages
import streamlit as st

#Heading
st.header("INDIAN RAILWAYS")

#Caption
st.caption("Safety | Security | Punctuality")

#Image
st.image("https://www.wallpapertip.com/wmimgs/155-1554570_indian-train-images-hd.jpg.jpg")

#Baloon Display
st.balloons()


#read file
import pandas as pd
import requests
url = "https://github.com/Vinotha27/Small_streamlit/blob/main/train_schedule.csv"
s = requests.get(url).content
c = pd.read_csv(s)
print(c.head(5))





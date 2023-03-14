#import Packages
import streamlit as st

st.header("INDIAN RAILWAYS")

#title    
st.set_page_config(
     layout="wide",
     initial_sidebar_state="expanded",
)

#Caption
st.caption("Safety | Security | Punctuality")

#Image
st.image("https://www.wallpapertip.com/wmimgs/155-1554570_indian-train-images-hd.jpg.jpg")

#Baloon Display
st.balloons()


#read file
import pandas as pd
url=('https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.csv')
df = pd.read_csv(url)
print(df.head(5))





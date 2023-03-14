#import Packages
import streamlit as st

#title    
st.header("INDIAN RAILWAYS")
st.set_page_config(
     page_title="INDIAN RAILWAYS",
     page_icon="https://th.bing.com/th?id=OIP.ca8nmh0N3R4U8fc7M5NytAHaHa&w=250&h=250&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=3.1&rm=2",
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






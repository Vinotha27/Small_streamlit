#import Packages
import streamlit as st
import pandas as pd

#Heading
st.title ("INDIAN RAILWAYS")

#Caption
st.caption("Safety | Security | Punctuality")

#Image
st.image("https://www.wallpapertip.com/wmimgs/155-1554570_indian-train-images-hd.jpg.jpg")

#Baloon Display
st.balloons()

#read file
url=("https://github.com/Vinotha27/Small_streamlit/blob/main/train_info.csv")
df = pd.read_csv(url)
print(df.head(5))






import streamlit as st
import pandas as pd 

st.image('https://www.mediasearch.co.th/new_ariticle/img/CCTV-security-article-cctv-camera--12-12-04.jpg')
st.header("การนำเสนอสถิติการเกิดอุบัติเหตุของประเทศไทย")

col1,col2=st.columns(2)

with col1:
    st.subheader("จำนวนผู้เสียชีวิต")
    st.write("2,5600")
with col2:
    st.subheader("จำนวนผู้เสียชีวิต")
    st.write("2,5600")

dt=pd.read_excel('data/DT01.xlsx')

st.write(dt.head(1))

st.write()
NumM=dt[dt['Sex']=='ชาย'].count()
NumF=dt[dt['Sex']=='หญิง'].count()

st.subheader('ชาย')
st.subheader(NumM[1])
st.subheader('หญิง')
st.subheader(NumF[1])
dtSex=[NumM[1],NumF[1]]
dtSexb=pd.DataFrame(dtSex,index=["ชาย","หญิง"])
st.bar_chart(dtSexb)
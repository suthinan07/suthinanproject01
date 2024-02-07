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

dt.pd.read_exel('data/DT01.xlsx')

st.write(dt.head(1))

#st.write()
NumM=dt[dt['Sex']=='ชาย'].count()
NumF=dt[dt['Sex']=='หญิง'].count()

dtSex=[NumM,NumF]
dtSexd=pd.DataFrame(dtSex)
st.bar_chart(dtSexd)
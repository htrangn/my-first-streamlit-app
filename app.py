import streamlit as st
import plotly.graph_objects as go

st.title("GIẢI PHƯƠNG TRÌNH BẬC NHẤT")
a = st.number_input('Tham số a')
b = st.number_input('Tham số b')

if st.button('Giải'):
  if (a!=0): st.write('Phương trình có 1 nghiệm', -b/a)
  if (a==0 and b==0): st.write('Phương trình có vô số nghiệm')
  if (a==0 and b!=0): st.write('Phương trình vô nghiệm')

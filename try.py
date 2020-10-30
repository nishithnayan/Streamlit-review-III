

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
st.title("Interactive Plots to visualize crime statistics in Berlin")
st.sidebar.title("SIDE BAR")
DATA_URL = (r"C:\Users\Admin\Documents\review III\Berlin_crimes.csv")
@st.cache(persist=True)

def load_data():
   data=pd.read_csv(DATA_URL)
   return data
data=load_data()
st.write(data)
select=st.sidebar.selectbox("VISULATIZATION TYPE",["Histogram","Piechart","Scatter Plot"],key=1)
st.markdown("Total crime statstics in every distict")

if not st.sidebar.checkbox("Hide",True,key=1):
    if select == "Histogram":
        fig=px.bar(data,x='District',y='Local',color='Local')
        st.plotly_chart(fig)
    elif select=="Scatter Plot":
        fig=px.scatter(data,x='District',y='Local',color='Local')
        st.plotly_chart(fig)
            
    else:
        fig=px.pie(data,values='Local' ,names='District')
        st.plotly_chart(fig)
st.markdown("Robbery count vs Location")

if not st.sidebar.checkbox("Hide",True,key=2):
    if select == "Histogram":
        fig=px.bar(data,x='Location',y='Robbery',color='Robbery')
        st.plotly_chart(fig)
    elif select=="Scatter Plot":
        fig=px.scatter(data,x='Location',y='Robbery',color='Robbery')
        st.plotly_chart(fig)
    else:
        fig=px.pie(data,values='Robbery' ,names='District')
        st.plotly_chart(fig)
st.markdown("Threat made vs Location")

if not st.sidebar.checkbox("Hide",True,key=3):
    if select == "Histogram":
        fig=px.bar(data,x='Location',y='Threat',color='Threat')
        st.plotly_chart(fig)
    elif select=="Scatter Plot":
        fig=px.scatter(data,x='Location',y='Threat',color='Threat')
        st.plotly_chart(fig)
    else:
        fig=px.pie(data,values='Threat' ,names='District')
        st.plotly_chart(fig)
st.markdown("Plot of Injury, Assault")

if not st.sidebar.checkbox("Hide",True,key=4):
    if select == "Histogram":
        x1=data['Injury']
        x2=data['Agg_assault']
        hist_data=[x1,x2]
        group_labels=['INJURY','AGGRAVATED ASSAULT']
        fig=ff.create_distplot(hist_data,group_labels)
        st.plotly_chart(fig)
    elif select=="Scatter Plot":
        fig=px.scatter(data,x='Agg_assault',y='Injury',color='Injury')
        st.plotly_chart(fig)
    else:
        st.subheader("PLot for AGGRAVATED ASSAULT")
        fig1=px.pie(data,values='Agg_assault' ,names='District')
        
        fig2=px.pie(data,values='Injury' ,names='District')
        st.plotly_chart(fig1)
        st.subheader("PLot for Injury")
        st.plotly_chart(fig2)
st.markdown("MAP")
#x1=data['X']
#x2=data['Y']
#x={'lat':x1,'lon':x2}
#df=pd.DataFrame(x)
st.map(data)

st.markdown("Comparison of Robberry in Different districts")
st.sidebar.subheader("Comparision")
choice=st.sidebar.multiselect('Select Districts:',('Mitte','Friedrichshain-Kreuzberg'
                                                   ,'Reinickendorf','Lichtenberg','Marzahn-Hellersdorf','Charlottenburg-Wilmersdorf','Spandau','Steglitz-Zehlendorf','Tempelhof-SchÃ¶neberg','NeukÃ¶lln','Treptow-KÃ¶penick'),key='0')
if len(choice)>0:
    data_mod=data[data.District.isin(choice)]
    fig_comp=px.histogram(data_mod,x='Robbery',y='District',histfunc='count',facet_col='Code',color='Robbery')
    st.plotly_chart(fig_comp)
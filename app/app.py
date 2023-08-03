import streamlit as st
import pandas as pd
import numpy as np
import datetime
from datetime import date


st.title("Web App fvj Stats")
st.markdown(
        '''
# Boas vindas ao meu app fvj Stats .
boas analises!!!!!!!!!!
'''
    )

st.sidebar.header("Leagues")
selected_league = st.sidebar.selectbox('League',['ALEMANHA - 2. BUNDESLIGA', 'ALEMANHA - BUNDESLIGA', 'BRASIL - SÉRIE A', 'BRASIL - SÉRIE B', 'BRASIL - SÉRIE C', 'BÉLGICA - LIGA JUPILER', 'ESPANHA - LALIGA', 'ESPANHA - LALIGA2',
                                                 'FRANÇA - LIGUE 1', 'INGLATERRA - PREMIER LEAGUE', 'ITÁLIA - SERIE A', 'ITÁLIA - SERIE B', 'JAPÃO - LIGA J1', 'MÉXICO - LIGA MX', 'NORUEGA - ELITESERIEN', 'PORTUGAL - LIGA PORTUGAL', 
                                                'PORTUGAL - LIGA PORTUGAL 2', 'SUÉCIA - ALLSVENSKAN', 'TURQUIA - SUPER LIG'])



def load_data(league):
  
  
  url = "https://github.com/Franciscovj/jogos_dia_nba/blob/main/dados_exportados.xlsx?raw=true"
  data = pd.read_excel(url)
  data = data[data['Liga'] == selected_league]
    
  return data

df = load_data(selected_league)



# Sidebar - Team selection
sorted_unique_team = sorted(df.Home.unique())
selected_team = st.sidebar.multiselect('Teams', sorted_unique_team, sorted_unique_team)

# Filtering data
df_filtered = df[(df.Home.isin(selected_team))]


st.subheader('DataFrame - '+selected_league)
st.dataframe(df_filtered)



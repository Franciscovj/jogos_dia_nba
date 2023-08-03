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
selected_league = st.sidebar.selectbox('League',['BOLIVIA - DIVISION PROFESIONAL', 'PARAGUAY - PRIMERA DIVISION', 'COLOMBIA - PRIMERA A', 'VENEZUELA - PRIMERA DIVISION', 'ECUADOR - LIGA PRO', 'IRELAND - PREMIER DIVISION', 'CHILE - PRIMERA DIVISION', 'PERU - LIGA 1', 'URUGUAY - PRIMERA DIVISION', 'JAPAN - J1 LEAGUE', 
                                                 'THAILAND - THAI LEAGUE 1', 'JAPAN - J2 LEAGUE', 'SOUTH KOREA - K LEAGUE 1', 'CHINA - SUPER LEAGUE', 'SOUTH KOREA - K LEAGUE 2', 'LITHUANIA - A LYGA', 'USA - MLS', 'ESTONIA - MEISTRILIIGA', 'USA - USL CHAMPIONSHIP', 'SWEDEN - SUPERETTAN', 'NORWAY - ELITESERIEN', 
                                                 'NORWAY - OBOS-LIGAEN', 'SWEDEN - ALLSVENSKAN', 'FINLAND - VEIKKAUSLIIGA', 
                                                 'ICELAND - BESTA-DEILD KARLA', 'BRAZIL - SERIE B', 'BRAZIL - SERIE A', 'BRAZIL - SERIE C', 'BRAZIL - SERIE D', 'ROMANIA - LIGA 1', 'BULGARIA - PARVA LIGA', 'CZECH REPUBLIC - 1. LIGA', 'DENMARK - SUPERLIGA', 'RUSSIA - PREMIER LEAGUE', 'SLOVENIA - PRVA LIGA',
                                                 'POLAND - EKSTRAKLASA', 'CROATIA - HNL', 'GERMANY - 3. LIGA', 'SERBIA - SUPER LIGA', 'SWITZERLAND - SUPER LEAGUE', 'MEXICO - LIGA MX', 'SWITZERLAND - CHALLENGE LEAGUE', 'BOSNIA AND HERZEGOVINA - PREMIER LEAGUE', 'SLOVAKIA - FORTUNA LIGA', 'DENMARK - 1ST DIVISION', 
                                                 'AUSTRIA - 2. LIGA', 'FRANCE - LIGUE 2', 'BELGIUM - JUPILER PRO LEAGUE', 'GERMANY - 2. BUNDESLIGA', 'AUSTRIA - BUNDESLIGA', 'ARGENTINA - LIGA PROFESIONAL', 'UKRAINE - PREMIER LEAGUE', 'ARMENIA - PREMIER LEAGUE', 'ROMANIA - LIGA 2', 'NETHERLANDS - EREDIVISIE',
                                                 'FRANCE - NATIONAL', 'SCOTLAND - CHAMPIONSHIP', 'BELGIUM - CHALLENGER PRO LEAGUE',
                                                 'ENGLAND - CHAMPIONSHIP', 'ENGLAND - NATIONAL LEAGUE', 'ENGLAND - LEAGUE TWO', 'SOUTH AFRICA - PREMIER LEAGUE', 'SCOTLAND - PREMIERSHIP', 'ENGLAND - LEAGUE ONE', 'SCOTLAND - LEAGUE TWO', 'SCOTLAND - LEAGUE ONE', 'MONTENEGRO - PRVA CRNOGORSKA LIGA',
                                                 'HUNGARY - OTP BANK LIGA', 'NETHERLANDS - EERSTE DIVISIE', 'FRANCE - LIGUE 1',
                                                 'NORTHERN IRELAND - NIFL PREMIERSHIP', 'ENGLAND - PREMIER LEAGUE', 'PORTUGAL - LIGA PORTUGAL', 'PORTUGAL - LIGA PORTUGAL 2', 'AZERBAIJAN - PREMIER LEAGUE', 'CROATIA - PRVA NL', 'TURKEY - 1. LIG', 'TURKEY - SUPER LIG', 'GERMANY - BUNDESLIGA', 'WALES - CYMRU PREMIER', 'SPAIN - LALIGA',
                                                 'SPAIN - LALIGA2', 'CYPRUS - FIRST DIVISION', 'MALTA - PREMIER LEAGUE', 'ITALY - SERIE B', "ISRAEL - LIGAT HA'AL", 'GREECE - SUPER LEAGUE', 'ITALY - SERIE A', 'BAHRAIN - PREMIER LEAGUE', 'EGYPT - PREMIER LEAGUE', 'AUSTRALIA - A-LEAGUE', 'INDIA - ISL'])



def load_data(league):
  
  
  url = "dados_exportados.xlsx"
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



import streamlit as st
import pandas as pd
import numpy as np
import datetime
from datetime import date


st.title("Web App fvj Stats")

st.sidebar.subheader("Selecione as colunas")

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


def mapa():
    ind = {
        'Indaiatuba': {'lat': -23.09, 'lon': -47.217778},
        'Manaus': {'lat': -3.1, 'lon': -60.016667},
    }

    df = pd.DataFrame(ind).transpose()

    st.title('Conexão Indaiatuba - Manaus')

    st.map(df)

def load_data(league):
  
  
  url = "https://github.com/Franciscovj/jogos_dia_nba/blob/main/dash_23.csv?raw=true"
  data = pd.read_csv(url)
  data = data[data['Liga'] == selected_league]
    
  return data

df = load_data(selected_league)



# Sidebar - Columns selection
sorted_unique_column = df.columns.to_list()

selected_column = st.sidebar.multiselect('Columns', sorted_unique_column, [
 'Liga', 'Date', 'Home', 'Away', 'Goals_H_HT', 'Goals_A_HT', 'FT_Goals_H', 'FT_Goals_A', 'FT_Odds_H', 'FT_Odds_D', 'FT_Odds_A', 'HT_Odds_H', 'HT_Odds_D', 'HT_Odds_A', 'FT_Odds_DC_X2', 
 'HT_Odds_Under05', 'HT_Odds_Under15', 'FT_Odds_Over25', 'FT_Odds_under25', 'FT_Odds_Under35', 'FT_Odds_BTTS_Yes'
])

# Sidebar - Team selection
sorted_unique_team = sorted(df.Home.unique())
selected_team = st.sidebar.multiselect('Teams', sorted_unique_team, sorted_unique_team)

# Filtering data
df_filtered = df[(df.Home.isin(selected_team))]
df_filtered = df_filtered[selected_column]

st.subheader('DataFrame - '+selected_league)
st.dataframe(df_filtered)

pages = {
    'Mapa': mapa,
   'liga': load_data(selected_league)


}
page = st.sidebar.selectbox('Escolha uma página', pages.keys())

if page:
    pages[page]()


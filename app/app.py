import streamlit as st
import pandas as pd
import numpy as np
import datetime
from datetime import date


st.title("Web App fvj Stats")
selected_date = st.sidebar.date_input('Select a date', date.today())
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
 'HT_Odds_Under05', 'HT_Odds_Under15', 'FT_Odds_Over25', 'FT_Odds_under25', 'FT_Odds_Under35', 'FT_Odds_BTTS_Yes',
 'FT_Odds_BTTS_No', 'Result_HT', 'FT_Result', 'Total_Goals_FT','Total_Goals_HT','p_H', 'p_D', 'p_A', 'p_Over', 'p_Under',
 'p_H__p_D', 'p_H__p_A', 'p_D__p_A', 'p_D__p_Over','p_D__p_Under', 'CV_HDA', 'CV_HD', 'CV_HA', 'CV_DA', 'CV_DO', 'Pontos_H', 'Pontos_A', 'PPJ_H',
 'PPJ_A', 'SG_H', 'SG_A', 'DP_Pontos_H', 'DP_Pontos_A', 'CV_Pontos_H', 'CV_Pontos_A', 'VG_H', 'VG_A', 'Media_VG_H', 'Media_VG_A', 'DesvPad_VG_H','DesvPad_VG_A', 'CV_VG_H', 'CV_VG_A',
 'CG_H', 'CG_A', 'Media_CG_H', 'Media_CG_A', 'DesvPad_CG_H', 'DesvPad_CG_A', 'CV_CG_H',
 'CV_CG_A', 'GM_H', 'GM_A', 'Media_GM_H', 'Media_GM_A', 'DP_GM_H', 'DP_GM_A', 'CV_GM_H', 'CV_GM_A', 'GS_H', 'GS_A', 'Media_GS_H', 'Media_GS_A', 'DP_GS_H', 'DP_GS_A', 'CV_GS_H',
 'CV_GS_A', 'Media_p_H', 'Media_p_A', 'DP_p_H', 'DP_p_A', 'CG_H_XP', 'CG_A_XP', 'DP_CG_H_XP', 'DP_CG_A_XP', 'VG_H_XP', 'VG_A_XP', 'DP_VG_H_XP', 'DP_VG_A_XP', 'GM_H_XP', 'GM_A_XP', 'CV_GM_H_XP',
 'CV_GM_A_XP', 'GS_H_XP', 'GS_A_XP', 'CV_GS_H_XP', 'CV_GS_A_XP', 'gols_sofridos_home', 'gols_sofridos_away', 
 'Over05_FT', 'Over05_HT', 'Under05_HT', 'Under15_HT', 'Over25_FT', 'Under25_FT', 'Under35_FT', 'Home_Win', 
 'Away_Win', 'Away_X2', 'home_X1', 'Draw', 'BTTS', 'BTTS_NO', 'Porc_Over05HT_Home',
 'Porc_Over05HT_Away', 'Porc_Under15HT_Home', 'Porc_Under15HT_Away', 'Porc_Over05FT_Home', 'Porc_Over05FT_Away',
 'Porc_draw_Home', 'Porc_draw_Away', 'Porc_Over25FT_Home', 'Porc_Over25FT_Away', 'Porc_BTTS_Home', 'Porc_BTTS_Away'])

# Sidebar - Team selection
sorted_unique_team = sorted(df.Home.unique())
selected_team = st.sidebar.multiselect('Teams', sorted_unique_team, sorted_unique_team)

# Filtering data
df_filtered = df[(df.Home.isin(selected_team))]
df_filtered = df_filtered[selected_column]

st.subheader('DataFrame - '+selected_league)
st.dataframe(df_filtered)




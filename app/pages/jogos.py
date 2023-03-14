
import streamlit as st
import pandas as pd
import numpy as np
import datetime
from datetime import date

st.title("Web App fvj Stats")

st.sidebar.header('Jogos do Dia')

dia = st.date_input(
    "Data de Análise",
    date.today())

def load_data_jogos():
    data_jogos = pd.read_csv("https://github.com/futpythontrader/YouTube/blob/main/Jogos_do_Dia_FlashScore/"+str(dia)+"_Jogos_do_Dia_FlashScore.csv?raw=true")
    data_jogos = data_jogos[["League","Date","Home","Away","FT_Odd_H","FT_Odd_D","FT_Odd_A","FT_Odd_Over25","FT_Odd_Under25","FT_Odd_Under35",
      "FT_Odd_BTTS_Yes","FT_Odd_BTTS_No"]]
    
    return data_jogos

df_jogos = load_data_jogos()


# Define o valor mínimo e máximo do controle deslizante com base na coluna "FT_Odd_H" do DataFrame
valor_minimo = float(df_jogos['FT_Odd_H'].min())
valor_maximo = float(df_jogos['FT_Odd_H'].max())

# Cria um controle deslizante com base no valor mínimo e máximo definidos acima
valor_selecionado = st.slider('Selecione os pontos', valor_minimo, valor_maximo)

# Filtra o DataFrame com base no intervalo selecionado no controle deslizante
df_filtrado = df_jogos.query("FT_Odd_H.between(@valor_minimo, @valor_selecionado)")

st.subheader("Dataframe: Jogos do Dia")
st.dataframe(df_jogos)
st.dataframe(df_filtrado)



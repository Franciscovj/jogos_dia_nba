import streamlit as st
import pandas as pd

# Definir estilo CSS para a tabela
table_style = """
<style>
.dataframe {
    font-family: Arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
}

.dataframe th, .dataframe td {
    border: 1px solid #dddddd;
    padding: 8px;
    text-align: left;
}

.dataframe th {
    background-color: #f2f2f2;
}
</style>
"""

st.title("Web App fvj Stats")
st.markdown(
    '''
    # Boas vindas ao meu app fvj Stats .
    boas análises!!!!!!!!!!
    '''
)

st.sidebar.header("Leagues")
selected_league = st.sidebar.selectbox('League', ['ALEMANHA - 2. BUNDESLIGA', 'ALEMANHA - BUNDESLIGA', 'BRASIL - SÉRIE A', 'BRASIL - SÉRIE B', 'BRASIL - SÉRIE C', 'BÉLGICA - LIGA JUPILER', 'ESPANHA - LALIGA', 'ESPANHA - LALIGA2',
                                                 'FRANÇA - LIGUE 1', 'INGLATERRA - PREMIER LEAGUE', 'ITÁLIA - SERIE A', 'ITÁLIA - SERIE B', 'JAPÃO - LIGA J1', 'MÉXICO - LIGA MX', 'NORUEGA - ELITESERIEN', 'PORTUGAL - LIGA PORTUGAL',
                                                 'PORTUGAL - LIGA PORTUGAL 2', 'SUÉCIA - ALLSVENSKAN', 'TURQUIA - SUPER LIG'])

def load_data(league):
    url = f"https://github.com/Franciscovj/jogos_dia_nba/blob/main/app/dados_exportados.csv?raw=true"
    data = pd.read_csv(url)
    data = data[data['League'] == selected_league]
    return data

df = load_data(selected_league)

# Sidebar - Team selection
sorted_unique_team = sorted(df.Home.unique())
selected_team = st.sidebar.multiselect('Teams', sorted_unique_team, sorted_unique_team)

# Filtering data
df_filtered = df[df.Home.isin(selected_team)]

st.subheader('DataFrame - ' + selected_league)
st.markdown(table_style, unsafe_allow_html=True)
st.dataframe(df_filtered)

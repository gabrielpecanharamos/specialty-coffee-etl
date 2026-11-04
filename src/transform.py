import pandas as pd
import numpy as np

def padronizar_colunas(df):
    df.columns = (
        df.columns
        .str.strip() 
        .str.lower() 
        .str.replace('.', ' ', regex=False)
        .str.replace(' ', '_') 
        .str.replace('___', '_') 
    )
    return df

def remover_colunas(df, colunas=None):
    if colunas is None:
        colunas = [
        'unnamed:_0', 'altitude', 'mill', 'ico_number',
        'harvest_year', 'owner_1', 'owner', 'lot_number', 'expiration'
    ]
    return df.drop(columns=colunas, errors='ignore')

def padronizar_textos(df):
    for col in df.select_dtypes(include=['object', 'string']):
        df[col] = df[col].str.strip().str.title()
    return df

def converter_datas(df, colunas_data):
    for col in colunas_data:
        if col in df.columns:
            datas_limpas = df[col].astype(str).str.replace(
                r"(\d+)(st|nd|rd|th)", r"\1", regex=True
            )
            df[col] = pd.to_datetime(datas_limpas, errors="coerce").dt.date
    return df

def limpar_altitudes(df, alt_min=500, alt_max=5000):
    condicao_invalida = (
        (df['altitude_low_meters'] < alt_min) | (df['altitude_low_meters'] > alt_max) |
        (df['altitude_high_meters'] < alt_min) | (df['altitude_high_meters'] > alt_max)
    )

    colunas_altitude = ['altitude_low_meters', 'altitude_high_meters', 'altitude_mean_meters']
    df.loc[condicao_invalida, colunas_altitude] = np.nan

    df['altitude_mean_meters'] = df[['altitude_low_meters', 'altitude_high_meters']].mean(axis=1)
    return df

def remover_outliers(df, nota_minima=50):
    df = df[df['total_cup_points'] >= nota_minima]
    return df

def aplicar_limpeza(df):
    df = padronizar_colunas(df)  
    df = remover_colunas(df) 
    df = padronizar_textos(df) 
    df = limpar_altitudes(df) 
    df = remover_outliers(df)  
    df = converter_datas(df, ["expiration", "grading_date"])

    if 'region' in df.columns:
        df['region'] = df['region'].replace(['Test', 'Teste'], np.nan)

    if 'bag_weight' in df.columns:
        peso = df.pop('bag_weight').astype(str)
        valor = peso.str.extract(r'(\d+\.?\d*)')[0].astype(float)
        df['bag_weight_kg'] = np.where(peso.str.contains('lb', case=False), (valor * 0.453592).round(2), valor)

    df = df.sort_values(by='total_cup_points', ascending=False).reset_index(drop=True)
    df.insert(0, 'ranking_global', df.index + 1)
    return df

def transform_data(df_arabica, df_robusta):
    df_arabica = aplicar_limpeza(df_arabica)
    df_robusta = aplicar_limpeza(df_robusta)

    filtro = (
    df_arabica['country_of_origin'].isna() & 
    df_arabica['certification_address'].str.contains('E493C36C2D076Bf273064F7Ac23Ad562Af257A25', case=False, na=False)
    )

    df_arabica.loc[filtro, 'country_of_origin'] = 'Colombia'
    return df_arabica, df_robusta
import pandas as pd

def extract_data():
    df_arabica = pd.read_csv('arabica_data.csv')
    df_robusta = pd.read_csv('robusta_data.csv')
    
    return df_arabica, df_robusta
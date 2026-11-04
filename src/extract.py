import pandas as pd

def extract_data():
    df_arabica = pd.read_csv('arabica_data_cleaned.csv')
    df_robusta = pd.read_csv('robusta_data_cleaned.csv')
    
    return df_arabica, df_robusta
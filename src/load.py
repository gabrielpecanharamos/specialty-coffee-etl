import duckdb
from sqlalchemy import create_engine

def load_data(df_arabica, df_robusta, db_target="duckdb", conn_string=None):
    """
    Carrega e armazena os dados limpos no banco de dados escolhido.
    Padrão: DuckDB local ('coffee.duckdb').
    Opção: SQL Server via SQLAlchemy.
    """
    db_target = db_target.lower()

    if db_target == "duckdb":
        con = duckdb.connect('coffee.duckdb')
        
        con.register('temp_arabica', df_arabica)
        con.register('temp_robusta', df_robusta)
        
        con.execute("CREATE OR REPLACE TABLE arabica AS SELECT * FROM temp_arabica")
        con.execute("CREATE OR REPLACE TABLE robusta AS SELECT * FROM temp_robusta")
        
        con.close()
        print("✅ Carga concluída com sucesso no DuckDB local ('coffee.duckdb')!")

    elif db_target == "sqlserver":
        if not conn_string:
            raise ValueError("Para o SQL Server, é necessário fornecer a 'conn_string'.")
        
        engine = create_engine(conn_string)
        df_arabica.to_sql('arabica', con=engine, if_exists='replace', index=False)
        df_robusta.to_sql('robusta', con=engine, if_exists='replace', index=False)
        print("✅ Carga concluída com sucesso no SQL Server!")

    else:
        raise ValueError(f"Banco '{db_target}' não suportado. Escolha 'duckdb' ou 'sqlserver'.")
import argparse
from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

def run_pipeline(db_target="duckdb", conn_string=None):
    """Orquestra a execução das três etapas do ETL."""
    print("⏳ 1/3 Extraindo dados...")
    df_arabica, df_robusta = extract_data()

    print("⏳ 2/3 Transformando dados...")
    df_arabica, df_robusta = transform_data(df_arabica, df_robusta)

    print(f"⏳ 3/3 Carregando dados no destino ({db_target})...")
    load_data(df_arabica, df_robusta, db_target=db_target, conn_string=conn_string)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Pipeline ETL de Café")

    parser.add_argument(
        "--target", "-t",
        type=str,
        default="duckdb",
        choices=["duckdb", "sqlserver"],
        help="Banco de dados de destino"
    )

    parser.add_argument(
        "--conn-string", "-c",
        type=str,
        default=None,
        help="String de conexão do SQL Server"
    )

    args = parser.parse_args()

    run_pipeline(db_target=args.target, conn_string=args.conn_string)
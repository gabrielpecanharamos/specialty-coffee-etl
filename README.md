# speciality-coffee-etl 

Este repositório contém o código e a documentação do pipeline ETL desenvolvido para o processamento de dados sobre variedades de café (**Arábica** e **Robusta**), além de consultas analíticas em SQL.

O objetivo foi estruturar um fluxo modular e automatizado para extração, limpeza e carga dos dados em banco relacional.

## Tecnologias Utilizadas

- **Linguagem:** Python
- **Manipulação de Dados:** Pandas
- **Armazenamento e Consultas:** DuckDB, SQL Server (via SQLAlchemy)

## Fonte dos Dados

Os arquivos de dados brutos (`.csv`) devem estar salvos no projeto:
- `arabica_data_cleaned.csv`
- `robusta_data_cleaned.csv`

## Estrutura do Pipeline

O tratamento dos dados e a orquestração do processo foram divididos em módulos para separar as responsabilidades de cada etapa:

1. **Extração (`src/extract.py`):**
   - Leitura dos arquivos CSV (`arabica_data_cleaned.csv` e `robusta_data_cleaned.csv`).

2. **Transformação (`src/transform.py`):**
   - Padronização de nomes de colunas e textos.
   - Tratamento de altitude e remoção de inconsistências.
   - Limpeza e conversão de tipos de dados.

3. **Carga e Armazenamento (`src/load.py`):**
   - Persistência em banco de dados (`DuckDB` ou `SQL Server`).
   - Criação e substituição das tabelas finais (`arabica` e `robusta`).

4. **Orquestração (`main.py`):**
   - Localizado na raiz do projeto, executa a sequência completa (Extração ➔ Transformação ➔ Carga).

## Consultas e Análises em SQL

Após a carga no banco de dados, utilizamos as tabelas `arabica` e `robusta` para consultas analíticas e prática de SQL:

- **Comparação de Qualidade:** Média da pontuação total por país de origem.
- **Análise por Variedade:** Consultas comparativas entre café Arábica e Robusta.
- **Filtros de Altitude:** Identificação de lotes produzidos em regiões de alta altitude.

## Como Executar

1. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

2. Execute o pipeline principal na raiz do projeto:
  ```bash
   python main.py
   ```

3. Caso queira direcionar a carga para o SQL Server:
   ```bash
   python main.py --target sqlserver --conn-string "SUA_STRING_DE_CONEXAO"
   ```
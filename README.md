# speciality-coffee-etl 

Este é um projeto ETL completo e modular, projetado para execução simples e direta, focado no processamento de dados de qualidade de cafés especiais das espécies Árabica e Robusta.

A proposta é simples e didática: transformar dados brutos em informação estruturada para análise, permitindo executar o projeto localmente em **DuckDB** com zero configuração ou num ambiente corporativo com **Microsoft SQL Server**.

## Conhecendo os Destinos de Carga

Para quem está a descarregar o repositório, o código já está 100% pronto. Apenas precisa de escolher em qual motor quer guardar e consultar os seus dados:

**Atenção:** Os ficheiros arabica_data.csv e robusta_data.csv devem estar guardados na mesma pasta dos scripts Python para que a execução funcione corretamente.

### DuckDB (Para Análises Locais e Rápidas)
É a opção ideal para quem quer apenas fazer o download do projeto e rodar tudo imediatamente sem precisar de instalar ou configurar servidores de bases de dados. Ao executar o script, o DuckDB cria automaticamente um ficheiro local chamado `coffee.duckdb` na raiz do projeto, contendo as tabelas `arabica` e `robusta` prontas para consulta.

### Microsoft SQL Server (Para Consultas e Análises Avançadas)
É a opção pensada para cenários empresariais, simulação de ambiente de produção. O script conecta-se ao seu serviço do SQL Server, cria automaticamente a base de dados `dados_cafe` (caso ainda não exista) e estrutura as tabelas com tipos de dados otimizados.

## Estrutura do Projeto

O repositório adota uma estrutura plana para garantir que pode abrir o VS Code e rodar os scripts imediatamente sem se preocupar com imports complexos de pastas:

```text
specialty-coffee-etl/
├── arabica_data.csv            # Dados brutos de cafés Árabica
├── robusta_data.csv            # Dados brutos de cafés Robusta
├── main_to_duckdb.py           # Script ETL para carregar no DuckDB
├── main_to_sqlserver.py        # Script ETL para carregar no SQL Server
├── requirements.txt            # Bibliotecas necessárias
├── README.md                   # Documentação do projeto
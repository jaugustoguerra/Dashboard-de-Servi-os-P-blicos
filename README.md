# Dashboard de Serviços Públicos

Este projeto é um dashboard interativo desenvolvido com Streamlit para visualizar e filtrar dados de serviços públicos armazenados em um banco de dados SQLite.

## Estrutura do Projeto

- `dashapigov.py`: Script principal que contém o código do dashboard.
- `requirements.txt`: Arquivo com as dependências necessárias para rodar o projeto.
- `servicos_publicos.db`: Banco de dados SQLite contendo os dados dos serviços públicos.

## Instalação

1. Clone o repositório para sua máquina local.
2. Crie um ambiente virtual (opcional, mas recomendado):
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```
3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

1. Execute o script `dashapigov.py`:
    ```sh
    streamlit run dashapigov.py
    ```
2. Acesse o dashboard no seu navegador através do endereço fornecido pelo Streamlit (geralmente `http://localhost:8501`).

## Funcionalidades

- **Filtros na Barra Lateral**: Filtre os serviços por órgão e palavra-chave.
- **Tabela de Dados**: Visualize os dados filtrados em uma tabela interativa.
- **Gráficos Interativos**: Veja a distribuição dos serviços gratuitos vs. pagos e a proporção de serviços por órgão.
- **Detalhes do Serviço**: Exiba detalhes específicos de um serviço selecionado.
- **Download de Dados**: Baixe os dados filtrados em formato CSV.

## Personalização

Você pode personalizar o estilo do dashboard editando o bloco de código CSS no início do arquivo `dashapigov.py`.

## Contribuição

Sinta-se à vontade para abrir issues e pull requests para melhorias e correções.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

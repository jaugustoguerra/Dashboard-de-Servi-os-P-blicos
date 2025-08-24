
# 📊 Dashboard de Serviços Públicos

Este projeto é um **dashboard interativo** desenvolvido em **Python** usando **Streamlit** e **SQLite**. Ele permite visualizar e analisar dados de serviços públicos obtidos de uma API, oferecendo filtros por órgão, palavras-chave e tipo (gratuito/pago), além de exibir gráficos e detalhes sobre os serviços selecionados.

---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e executar o projeto localmente.

### Pré-requisitos

Antes de começar, verifique se você tem os seguintes itens instalados:

- **Python 3.8 ou superior**
- Bibliotecas Python:
  - `streamlit`
  - `pandas`
  - `plotly`
 

### Passos para Configuração

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/dashboard-servicos-publicos.git
   cd dashboard-servicos-publicos
   ```

2. **Crie um ambiente virtual** (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados:**

   O projeto utiliza um banco de dados SQLite chamado `servicos_publicos.db`. Certifique-se de que o banco de dados esteja configurado corretamente e contenha a tabela `servicos` com os dados necessários.

5. **Execute o dashboard:**

   ```bash
   streamlit run dashapigov.py
   ```

6. **Acesse o dashboard:**

   Abra seu navegador e acesse `http://localhost:8501` para visualizar o dashboard em funcionamento.

---

## 🛠️ Funcionalidades do Dashboard

- **Filtros:**
  - **Selecionar Órgão**: Filtra os serviços por órgão responsável. Inclui a opção "Mais de 100 Serviços" para exibir apenas órgãos com mais de 100 serviços.
  - **Palavras-chave**: Filtra os serviços que contêm uma determinada palavra-chave.

- **Visualizações:**
  - **Tabela de Serviços Filtrados**: Exibe os serviços filtrados em uma tabela interativa.
  - **Gráfico de Barras**: Mostra a distribuição de serviços gratuitos e pagos por órgão.
  - **Detalhes do Serviço**: Exibe informações detalhadas sobre um serviço selecionado.

- **Botão de Download:**
  - **Baixar Dados Filtrados**: Permite baixar os dados filtrados em formato CSV.

---

## 🧩 Estrutura do Projeto

- `dashapigov.py`: Código principal do dashboard.
- `servicos_publicos.db`: Banco de dados SQLite contendo os dados dos serviços públicos.
- `README.md`: Documentação do projeto (este arquivo).
- `requirements.txt`: Lista de dependências do projeto.

---

## 📊 Tecnologias Utilizadas

- **Streamlit**: Framework para criar aplicações web interativas em Python.
- **SQLite**: Banco de dados leve e embutido para armazenar os dados dos serviços.
- **Pandas**: Biblioteca para manipulação e análise de dados.
- **Plotly**: Biblioteca para criação de gráficos interativos.

---

## 📝 Como Contribuir

1. Faça um **fork** deste repositório.
2. Crie uma **branch** para sua feature:
   ```bash
   git checkout -b feature/nova-feature
   ```
3. Faça **commit** das suas alterações:
   ```bash
   git commit -m 'Adiciona nova feature'
   ```
4. **Push** para a branch:
   ```bash
   git push origin feature/nova-feature
   ```
5. Abra um **Pull Request**.

---

## 📄 Licença

Este projeto está licenciado sob a licença **MIT**. Consulte o arquivo `LICENSE` para mais detalhes.

---

## 🤝 Contato

Se você tiver dúvidas ou sugestões, sinta-se à vontade para entrar em contato:

- **Nome**: José Augusto Guerra
- **E-mail**: [auguscontas@gmail.com]
- **GitHub**: [jaugustoguerra](https://github.com/jaugustoguerra)
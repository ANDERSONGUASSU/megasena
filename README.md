# Gerador de Jogos da Mega-Sena

Este é um projeto Python que gera e gerencia combinações de números para jogos da Mega-Sena. O projeto utiliza um banco de dados SQLite para armazenar todas as possíveis combinações de números (50.063.860 combinações no total) e fornece uma interface de linha de comando (CLI) para interagir com os dados.

## Funcionalidades

- Geração de todas as combinações possíveis de jogos da Mega-Sena (6 números entre 1 e 60)
- Armazenamento eficiente das combinações em banco de dados SQLite
- Interface de linha de comando interativa usando Typer e Rich
- Processamento em lotes para gerenciamento eficiente de memória

## Requisitos

- Python 3.11+
- Dependências listadas em `requirements.txt`

## Instalação

1. Clone o repositório:
   ```bash
   git clone [url-do-repositorio]
   cd megasena
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   # ou
   .venv\Scripts\activate  # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

O projeto oferece uma interface de linha de comando com os seguintes comandos:

1. Inicializar o banco de dados:
   ```bash
   python main.py init-db
   ```

2. Gerar todas as combinações possíveis:
   ```bash
   python main.py gerar-jogos
   ```
   ⚠️ Atenção: Este comando irá gerar 50.063.860 combinações!

3. Visualizar jogos cadastrados:
   ```bash
   python main.py mostrar-jogos
   ```

## Estrutura do Projeto

```
megasena/
├── main.py              # Ponto de entrada da aplicação
├── requirements.txt     # Dependências do projeto
├── setup.cfg           # Configurações de desenvolvimento
└── src/
    ├── cli/            # Interface de linha de comando
    │   └── commands.py # Implementação dos comandos
    ├── core/           # Lógica principal
    │   ├── combinacoes.py  # Geração de combinações
    │   └── ids.py      # Geração de IDs únicos
    ├── data/           # Dados persistentes
    │   └── megasena.db # Banco de dados SQLite
    └── storage/        # Camada de acesso a dados
        └── sqlite.py   # Operações com banco de dados
```

## Desenvolvimento

O projeto segue as melhores práticas de desenvolvimento Python:

- Tipagem estática com MyPy
- Formatação de código com Black
- Linting com Flake8
- Documentação em docstrings
- Testes automatizados (em desenvolvimento)

## Configurações

O arquivo `setup.cfg` contém configurações para:
- Flake8: limite de linha em 109 caracteres
- MyPy: verificação rigorosa de tipos
- Pylint: configurações personalizadas para linting

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.


## Contribuições

Contribuições são bem-vindas! Por favor, sinta-se à vontade para submeter pull requests ou abrir issues para discussão.

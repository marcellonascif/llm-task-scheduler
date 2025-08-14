# LLM Task Scheduler

Este projeto explora o uso do Gemini (Google Generative AI) para gerar automaticamente planos de ação a partir de prompts de tarefas submetidos pelo usuário. Comparamos duas abordagens: uma baseline que cria um plano de ação simples sem decompor a tarefa, e outra que decompõe a tarefa em subtarefas detalhadas. O objetivo é analisar e comparar a eficácia de ambas as estratégias para cenários de gerenciamento de tarefas pessoais.

## Pré-requisitos

- Python 3.11 ou superior
- Poetry (gerenciador de dependências)
- Chave de API do Google Gemini

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/marcellonascif/llm-vs-rn.git
cd llm-vs-rn
```

### 2. Instale o Poetry

Siga as instruções de instalação do [Poetry](https://python-poetry.org/docs/).

### 3. Instale as dependências

```bash
poetry install
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```bash
cp .env.example .env
```

Edite o arquivo `.env` e adicione sua chave de API do Gemini:

```
GEMINI_API_KEY=sua_chave_api_aqui
```

## Execução

### Executar notebooks Jupyter

Para executar os notebooks de análise:

```bash
poetry run jupyter lab
```

#### Pipeline de processamento de dados

Execute os notebooks na seguinte ordem para gerar os arquivos CSV:

1. **Preparação inicial dos dados:**
   - `notebooks/drop_columns.ipynb` - Remove colunas desnecessárias dos dados originais
   - `notebooks/summary.ipynb` - Gera sumários e análises dos dados

2. **Processamento e formatação:**
   - `notebooks/convert_data.ipynb` - Converte `tasks_summary.csv` para formato compatível
   - `notebooks/translate_task.ipynb` - Traduz tarefas para inglês, gera `data/fixed/translated_tasks.csv`
   - `notebooks/verbalize_summary.ipynb` - Verbaliza sumários, gera `data/fixed/verbalized_tasks.csv`

3. **Análise com modelos LLM:**
   - `notebooks/llm/gpt.ipynb` - Executa inferências com modelos LLM, gera arquivos em `data/results/`
   - `notebooks/llm/metrics.ipynb` - Calcula métricas de performance, gera `metrics_summary.csv`

#### Estrutura dos notebooks por pasta:
- `notebooks/`: Notebooks de processamento e análise geral
- `notebooks/llm/`: Notebooks específicos para modelos LLM e métricas
- `notebooks/nesa/`: Notebooks específicos para análise NESA

### Arquivos gerados

O pipeline gera os seguintes arquivos CSV:

#### Resultados de experimentos (`data/results/`):
- `10_last_tasks_scheduling_results.csv` - Resultados das últimas 10 tarefas
- `week_scheduling_results.csv` - Resultados de agendamento semanal
- `month_scheduling_results.csv` - Resultados de agendamento mensal

#### Dados de análise (raiz `data/`):
- `inference_data.csv` - Dados preparados para inferência
- `metrics_summary.csv` - Sumário das métricas de performance
- `summary_calendar_unique.csv` - Sumários únicos por calendário

## Configuração

O projeto utiliza arquivos YAML para configuração de prompts:
- `scheduler.prompt.yml`: Configuração do prompt do agendador
- `verbalizer.prompt.yml`: Configuração do prompt do verbalizador


## Estrutura do projeto

```
├── notebooks/          # Notebooks Jupyter para análise
│   ├── llm/           # Notebooks específicos para modelos LLM
│   └── nesa/          # Notebooks específicos para análise NESA
├── data/              # Dados e resultados
│   ├── fixed/         # Dados processados e formatados
│   └── results/       # Resultados dos experimentos
├── scheduler.prompt.yml # Configuração do prompt do agendador
├── verbalizer.prompt.yml # Configuração do prompt do verbalizador
├── pyproject.toml     # Configuração do Poetry
└── README.md          # Este arquivo
```

# Comparação de Técnicas para Resolução de Problemas de Grafos: IA Clássica (BFS) vs LLM (Gemini)

Este projeto compara duas abordagens para resolver **problemas de busca em grafos descritos em linguagem natural**: uma baseada em **IA Clássica** (Busca em Largura e busca por pais), e outra baseada em uma **LLM da Google (Gemini)**.

---

## Objetivo

Implementar e comparar:

1. Uma técnica de **IA Clássica** usando **algoritmos puros** para BFS e busca de pais em grafos.
2. Uma técnica baseada em **LLM**, utilizando a **API Gemini** da Google.
3. Um relatório comparativo com acurácia, erros e prompts mal resolvidos.

---

## Estrutura do Projeto

```
project_root/
├── .env                      # Contém a chave da API do Gemini (NÃO versionar)
├── .gitignore                # Ignora arquivos como .env, __pycache__, etc.
├── requirements.txt          # Dependências do projeto
├── run.sh                    # Script para executar o pipeline completo
├── prompts.csv               # Arquivo com todos os prompts a serem processados
│
├── database.py               # Gera o arquivo prompts.csv a partir do dataset
│
├── classic_ai/               # Implementação da IA clássica
│   ├── __init__.py
│   ├── classic_ai.py
│   └── classic_ai_answers.csv
│
├── llm/                      # Implementação com modelo LLM (Gemini)
│   ├── llm.py
│   └── llm_answers.csv
│
├── evaluation/               # Comparação entre IA clássica e LLM
│   ├── compare_results.py
│   └── comparison_report.csv
│
├── utils/                    # Funções auxiliares e parsing
│   ├── __init__.py
│   ├── prompt_parser.py
│   └── test_cases.py

````

---

## Requisitos

- Python 3.8+
- Altere o arquivo `.env` na raiz com sua chave da API do Gemini:

```bash
GOOGLE_API_KEY="SUA_CHAVE_AQUI"
````

* Instale as dependências com:

```bash
pip install -r requirements.txt
```

---

## Como Executar

1. Dê permissão de execução ao script:

```bash
chmod +x run.sh
```

2. Execute tudo com um só comando:

```bash
./run.sh
```

Esse script executa as seguintes etapas:

* Baixa e prepara o dataset (`database.py`)
* Processa os prompts com IA Clássica (`classic_ai.py`)
* Processa os prompts com LLM (Gemini) (`llm.py`)
* Compara os resultados e gera um relatório final (`compare_results.py`)

---

## Dataset

O dataset vem do Hugging Face: [`openai/graphwalks`](https://huggingface.co/datasets/openai/graphwalks)

Para testes, o `database.py` pode ser configurado para carregar menos exemplos de **`bfs`** e `parents`**:

```python
# ================= INÍCIO DO TRECHO DE TESTE =================
df = pd.concat([
    df[df["problem_type"] == "parents"].head(25),
    df[df["problem_type"] == "bfs"].head(25)
])
# ================== FIM DO TRECHO DE TESTE ===================
```

> Remova esse trecho para usar o dataset completo.

---

## Técnicas Utilizadas

### IA Clássica

* Implementação manual de:

  * `bfs(graph, start_node, depth)`
  * `find_parents(graph, target_node)`
* Extração de arestas e parâmetros com regex (`utils/prompt_parser.py`)
* Resultados salvos em `classic_ai/classic_ai_answers.csv`

### LLM (Gemini)

* Envia o prompt completo para o modelo `gemini-1.5-flash`
* Extrai a linha `Final Answer: [...]` via regex
* Resultados salvos em `llm/llm_answers.csv`

---

## Avaliação

Arquivo final gerado: `evaluation/comparison_report.csv`

Campos:

```csv
method,problem_type,accuracy,num_correct,num_wrong,wrong_prompt_ids
classic_ai,bfs,0.8,8,2,[5,9]
llm,parents,0.7,7,3,[2,6,10]
...
```

---

## Notas Finais

* O código foi modularizado para facilitar manutenção e testes.
* A validação considera `set(expected) == set(predicted)`, ignorando a ordem.

---

## Autoria

Projeto desenvolvido pelos alunos de **Ciência da Computação** da **UFF** **Júlia Câmara** e **Pedro Albuquerque**, para a disciplina **Inteligência Artificial** ministrada pela professora **Aline Paes**.

```

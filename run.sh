#!/bin/bash

set -e

source .env

echo "Limpando arquivos de saída anteriores..."
rm -f prompts.csv
rm -f classic_ai/classic_ai_answers.csv
rm -f llm/llm_answers.csv
rm -f evaluation/comparison_report.csv

echo "Passo 1: Gerando prompts.csv a partir do dataset..."
python database.py

echo "Passo 2: Rodando IA Clássica (BFS + Parents)..."
python classic_ai/classic_ai.py

echo "Passo 3: Rodando LLM (Gemini)..."
python llm/llm.py

echo "Passo 4: Comparando resultados..."
python evaluation/compare_results.py

echo "Tudo pronto! Resultados salvos em:"
echo "  - prompts.csv"
echo "  - classic_ai/classic_ai_answers.csv"
echo "  - llm/llm_answers.csv"
echo "  - evaluation/comparison_report.csv"

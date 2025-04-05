# Gerador-Bloco-de-Blockchain
Simulador de geração e mineração de blocos fictícios em uma blockchain com validação de hash e registro em JSON.

# Simulador de Blockchain em Python

Este projeto é um simulador didático de uma blockchain fictícia, criado com Python.

## Funcionalidades

- Geração de blocos com dados personalizados
- Cálculo de hash com SHA-256
- Validação de blocos por dificuldade (nível de zeros no início da hash)
- Armazenamento em `blocos.json`
- Validação encadeada da integridade (hash anterior)
- Simulação de mineração automática com log em `log.txt`
- Recompensa simbólica de 3,125 BTC por bloco minerado

## Arquivos principais

- `gerador.py`: Gera novos blocos
- `minerador.py`: Minera blocos pendentes
- `blocos.json`: Armazena a blockchain
- `log.txt`: Log de mineração e recompensas

## Requisitos

- Python 3.10+
- Biblioteca padrão `hashlib`, `datetime`, `json`, `random`, `os`, `time`

## Como usar

1. Execute `gerador.py` para adicionar um novo bloco
2. Execute `minerador.py` para minerar blocos pendentes
3. Consulte `log.txt` para acompanhar os resultados

---

> Projeto criado para fins educacionais, sem intenção de uso financeiro real.

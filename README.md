# Sprint 3 – Dynamic Programming (ClinMind)

Este projeto é a entrega da Sprint 3 para a disciplina de Dynamic Programming, parte do **Challenge DASA + FIAP**.  
O objetivo foi aplicar os conceitos fundamentais de **estruturas de dados** e **algoritmos clássicos** em um programa **interativo** em Python, simulando o **controle de consumo de insumos** em um laboratório.

> Observação: o código usa apenas conteúdos vistos em aula.  
> As datas seguem o formato **`ddmmyy`** (ex.: `010925`).

## 🚀 Como executar
1. Tenha o **Python 3** instalado.  
2. Baixe o arquivo `sprint3.py` (ou clone o repositório).  
3. No terminal, execute: `python sprint3.py`.

## 🧭 Menu (resumo exato)
- `1` Registrar consumo (datas `ddmmyy`)  
- `2` Atender Fila (FIFO)  
- `3` Desfazer último da Pilha (LIFO)  
- `4` Mostrar Fila  
- `5` Mostrar Pilha (topo primeiro)  
- `6` Ordenar por QUANTIDADE (Merge) em **todos os dados**  
- `7` Ordenar por VALIDADE (Quick) em **todos os dados**  
- `8` Busca SEQUENCIAL (NOME/LOTE)  
- `9` Busca BINÁRIA (NOME, com lista ordenada por nome)  
- `0` Sair

> Nota: Fila e Pilha são estruturas operacionais; as opções **6/7** ordenam uma **cópia da lista base `dados`** para manter a demonstração mesmo que Fila/Pilha estejam vazias.

## 🗂️ Estrutura dos dados
Cada registro é um dicionário com:
- `id` (inteiro sequencial)  
- `nome` (texto do insumo)  
- `lote` (código)  
- `validade` (`ddmmyy`)  
- `data` (`ddmmyy`)  
- `qtd` (inteiro não negativo)

## 🧠 Como cada estrutura/algoritmo foi usado
- **Fila (FIFO):** atendimento em ordem cronológica (entra no fim com `append`; sai do início com `pop(0)`).  
- **Pilha (LIFO):** manipulação do item mais recente (entra no topo com `append`; sai do topo com `pop()`).  
- **Busca Sequencial:** percorre toda a lista para encontrar **NOME** ou **LOTE** (retorna todos os índices).  
- **Busca Binária (por NOME):** após ordenar por nome (Merge), busca com ponteiros `inicio`, `fim` e `meio`.  
- **Merge Sort (por `qtd`):** divide, ordena recursivamente e intercala (ordem crescente).  
- **Quick Sort (por `validade`):** partição por pivô; comparação de `ddmmyy` feita de forma didática (ano → mês → dia).

## 📋 Requisitos atendidos
- Interação via `while`/`input` (sem `main`, sem libs externas).  
- Operações de lista: `append`, `pop(0)`, `pop()`.  
- Buscas: sequencial e binária.  
- Ordenações: Merge Sort e Quick Sort (recursivos).  
- Datas no padrão `ddmmyy`, com validação simples (dígitos e faixas de dia/mês).

## 👥Turma: 2ESPI - Integrantes
- **Bruno Carneiro Leão** — RM 555563 (2ESPV)  
- **Guilherme da Cunha Melo** — RM 555310 (2ESPI)  
- **Matheus Gushi Morioka** — RM 556935 (2ESPI)  
- **Paulo Akira Okama** — RM 556840 (2ESPI)

## 🔗 Repositório
https://github.com/pauloakira05/sprint3_dynamic_programming_clinmind

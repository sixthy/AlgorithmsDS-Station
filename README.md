# AED Station / Algorithms and Data Structures Station

Projeto desenvolvido em Python como estudo prático de Algoritmos e Estruturas de Dados.

O objetivo do projeto é simular o funcionamento básico de uma estação ferroviária, trabalhando conceitos como passageiros, viagens, comboios, bilheteira, filas, pilhas, leitura de ficheiros CSV e geração de resultados em arquivos de saída.

Este projeto foi desenvolvido para um trabalho de faculdade, sendo para praticar lógica de programação, organização de módulos e uso de estruturas de dados.

---

## Tecnologias utilizadas

- Python
- CSV
- Programação orientada a objetos
- Estruturas de dados
- Filas
- Pilhas
- Manipulação de arquivos
- Leitura e escrita de ficheiros `.csv`

---

## Funcionalidades

- Leitura de dados a partir de arquivos CSV
- Simulação de passageiros
- Simulação de viagens
- Simulação de comboios
- Controle de bilheteira
- Organização de passageiros em filas
- Uso de pilhas para armazenamento temporário de dados
- Gestão de uma estação
- Geração de arquivos de saída
- Registro de erros em arquivos `.txt`
- Processamento de dados de entrada e exportação dos resultados

---

## Estrutura principal do projeto

```txt
aedStation/
├── main.py
├── bilheteira.py
├── comboio.py
├── estacao.py
├── fila.py
├── passageiro.py
├── pilha.py
├── tempo.py
├── viagem.py
├── texto_reescrito.txt
│
├── Input/
│   └── Problema1/
│       ├── parametros.csv
│       ├── parque.csv
│       ├── passageiros.csv
│       ├── questoes_seguidores.csv
│       └── viagens.csv
│
├── Output/
│   ├── erro.txt
│   └── Problema1/
│       ├── erro.txt
│       ├── parque.csv
│       ├── passageiros.csv
│       ├── placar.csv
│       ├── questoes_seguidores.csv
│       └── viagens.csv
│
└── __pycache__/
```

---

## Objetivo do projeto

O projeto tem como objetivo simular uma estação ferroviária utilizando conceitos aprendidos em Algoritmos e Estruturas de Dados.

Durante o desenvolvimento, foram praticados conceitos como:

- Criação de classes
- Separação de responsabilidades por arquivos
- Leitura de dados externos
- Escrita de resultados
- Uso de filas
- Uso de pilhas
- Manipulação de passageiros e viagens
- Organização de dados em memória
- Simulação de processos
- Tratamento básico de erros

---

## Como funciona

O fluxo principal do projeto é:

1. O programa é iniciado pelo arquivo `main.py`.
2. Os dados de entrada são lidos da pasta `Input/Problema1/`.
3. As informações de passageiros, viagens, parque e parâmetros são carregadas.
4. O sistema processa os dados da estação.
5. As estruturas de dados são utilizadas para organizar o fluxo.
6. Os resultados são gerados na pasta `Output/Problema1/`.
7. Caso existam erros, eles são registrados em arquivos `.txt`.

---

## Arquivos principais

### main.py

Arquivo principal do projeto.

Responsável por iniciar a execução do programa e chamar a lógica principal da estação.

---

### estacao.py

Contém a lógica principal da estação.

Este arquivo centraliza grande parte do comportamento do sistema, incluindo o processamento dos passageiros, viagens, comboios e resultados.

---

### bilheteira.py

Representa a lógica relacionada à bilheteira da estação.

Pode ser usada para controlar atendimento, bilhetes ou interações relacionadas aos passageiros.

---

### comboio.py

Representa o comboio dentro da simulação.

Pode armazenar ou controlar informações relacionadas aos comboios utilizados nas viagens.

---

### passageiro.py

Define a estrutura de um passageiro.

Pode conter dados como identificação, nome, destino, viagem ou outras informações necessárias para o fluxo do sistema.

---

### viagem.py

Representa uma viagem dentro da estação.

Pode conter dados relacionados ao trajeto, horário, comboio ou passageiros associados.

---

### fila.py

Implementa uma estrutura de dados do tipo fila.

Filas seguem o princípio FIFO:

```txt
First In, First Out
```

Ou seja, o primeiro elemento a entrar é o primeiro a sair.

---

### pilha.py

Implementa uma estrutura de dados do tipo pilha.

Pilhas seguem o princípio LIFO:

```txt
Last In, First Out
```

Ou seja, o último elemento a entrar é o primeiro a sair.

---

### tempo.py

Contém funções ou estruturas relacionadas ao controle de tempo da simulação.

Pode ser usado para comparar horários, controlar duração ou organizar eventos.

---

## Pastas do projeto

### Input

A pasta `Input/` contém os arquivos de entrada usados pelo programa.

Dentro dela existe a pasta `Problema1/`, com os seguintes arquivos:

```txt
parametros.csv
parque.csv
passageiros.csv
questoes_seguidores.csv
viagens.csv
```

Esses arquivos fornecem os dados necessários para a execução da simulação.

---

### Output

A pasta `Output/` contém os arquivos gerados pelo programa após a execução.

Dentro dela existe a pasta `Problema1/`, com arquivos como:

```txt
erro.txt
parque.csv
passageiros.csv
placar.csv
questoes_seguidores.csv
viagens.csv
```

Esses arquivos representam os resultados processados pela aplicação.

---

## Pré-requisitos

Antes de rodar o projeto, instale:

- Python 3

Verifique se o Python está instalado:

```bash
python --version
```

ou:

```bash
python3 --version
```

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/sixthy/aedStation.git
```

Entre na pasta do projeto:

```bash
cd aedStation
```

Caso queira usar ambiente virtual, crie um ambiente com:

```bash
python -m venv .venv
```

Ative o ambiente virtual no Windows:

```bash
.venv\Scripts\activate
```

Ative o ambiente virtual no Linux/Mac:

```bash
source .venv/bin/activate
```

---

## Rodando o projeto

Execute o arquivo principal:

```bash
python main.py
```

ou:

```bash
python3 main.py
```

O programa irá ler os arquivos da pasta `Input/Problema1/` e gerar os resultados na pasta `Output/Problema1/`.

---

## Exemplo de fluxo

1. O arquivo `parametros.csv` define configurações iniciais.
2. O arquivo `passageiros.csv` fornece os dados dos passageiros.
3. O arquivo `viagens.csv` fornece os dados das viagens.
4. O programa processa os dados usando as classes e estruturas criadas.
5. Os resultados são salvos em arquivos CSV dentro da pasta `Output/Problema1/`.
6. Caso ocorra algum problema, os erros são registrados em `erro.txt`.

---

## Conceitos praticados

Este projeto trabalha conceitos importantes de Algoritmos e Estruturas de Dados, como:

- Classes e objetos
- Modularização
- Estruturas lineares
- Fila
- Pilha
- Leitura de arquivos
- Escrita de arquivos
- Processamento de CSV
- Simulação de eventos
- Organização de dados
- Separação entre entrada, processamento e saída

---

## Comandos úteis

Executar o projeto:

```bash
python main.py
```

Executar com Python 3:

```bash
python3 main.py
```

Criar ambiente virtual:

```bash
python -m venv .venv
```

Ativar ambiente virtual no Windows:

```bash
.venv\Scripts\activate
```

Ativar ambiente virtual no Linux/Mac:

```bash
source .venv/bin/activate
```

Gerar arquivo de dependências:

```bash
pip freeze > requirements.txt
```

---

## Status

Projeto desenvolvido como estudo e prática de Algoritmos e Estruturas de Dados.

Implementados:

- Leitura de arquivos CSV
- Processamento de dados da estação
- Classes para entidades principais
- Estrutura de fila
- Estrutura de pilha
- Geração de arquivos de saída
- Registro de erros
- Organização modular do código

---

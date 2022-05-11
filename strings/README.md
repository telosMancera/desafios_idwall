# Desafio 1: Strings

## 1. Enunciado

Após ler o coding style do kernel Linux, você descobre a mágica que é
ter linhas de código com no máximo 80 caracteres cada uma.

Assim, você decide que de hoje em diante seus e-mails enviados também
seguirão um padrão parecido e resolve desenvolver um plugin para te ajudar
com isso. Contudo, seu plugin aceitará no máximo 40 caracteres por linha.

Implemente uma função que receba:
1. um texto qualquer
2. um limite de comprimento

e seja capaz de gerar os outputs dos desafios abaixo.

### 1.1. Exemplo input

`In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.`

`And God said, "Let there be light," and there was light. God saw that the light was good, and he separated the light from the darkness. God called the light "day," and the darkness he called "night." And there was evening, and there was morning - the first day.`

O texto deve ser parametrizável e se quiser, pode utilizar um texto de input de sua preferência.

### 1.2. Parte 1 (Básico) - limite 40 caracteres
Você deve seguir o exemplo de output [deste arquivo](https://github.com/idwall/desafios/blob/master/strings/output_parte1.txt), onde basta o texto possuir, no máximo, 40 caracteres por linha. As palavras não podem ser quebradas no meio.

### 1.3. Parte 2 (Intermediário) - limite 40 caracteres
O exemplo de output está [neste arquivo](https://github.com/idwall/desafios/blob/master/strings/output-parte2.txt), onde além de o arquivo possuir, no máximo, 40 caracteres por linha, o texto deve estar **justificado**.

## 2. Solução

### 2.1. Estrutura

Segue abaixo a estrura de arquivos utilizada.

```
strings/
|- pyformatter/ - Package python principal da solução
|  |- __init__.py
|  |- __main__.py - Entry point do script
|  |- formatter.py - Formator de strings
|  |- functions.py - Funções chamadas no entry point
|  |- settings.py - Configurações gerais
|  |- utils.py - Funções para uso geral
|
|- requirements/ - Dependências python
|  |- base.txt - Dependências básicas
|  |- bot.txt - Dependências utilizadas apenas pelo bot
|  |- cli.txt - Dependências utilizadas apenas pelo cli
|  |- development.txt - Dependências para desenvolvimento
|
|- tests/ - Testes unitários
|  |- test_crawlers/ - Testes dos crawlers
|  |  |- test_reddit.py - Testes com RedditCrawler
|  |
|  |- conftest.py - Fixtures (pytest) utilizads nos testes
|  |- test_functions.py - Testes das funções definidas em crawler/functions.py
|
|- Makefile - Comandos para instalação de dependências
|- pytest.ini - Configuração de execução do pytest
|- README.md - Este README
```

### 2.2. Executando a solução

#### 2.2.1. Instalando as dependências

> Nota: A solução foi desenvolvida com python3.9. Para a utilização de outra versão, basta alterar a constante **PYTHON_VERSION**, encontrada em **Makefile**

Para a instalação das dependências basta executar o seguinte comando:

```bash
make install
```

Caso queira instalar também as dependências para desenvolvimento:

```bash
make develop
```

#### 2.2.2. Execução em si

Antes de executar o script, é necessária a ativação do **venv** do python.

```bash
. ./venv/bin/activate
```

**CLI**

A utilização básica do script é feita através de:

```bash
python -m pyformatter 'Texto a ser formatado por este belo e elegante formatador!'
```

Para maiores detalhes na utilização completa, execute

```bash
python -m pyformatter -h
```

#### 2.2.3. Executando os testes unitários

Para a execução dos testes unitários, é necessário ter instalado as dependências de desenvolvimento. Vide seção [2.2.1. Instalando as dependências](#221-instalando-as-dependências).

Execute:

```bash
make tests
```

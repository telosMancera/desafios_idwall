# Desafio 2: Crawlers

## 1. Enunciado

Parte do trabalho na IDwall inclui desenvolver *crawlers/scrapers* para coletar dados de websites.
Como nós nos divertimos trabalhando, às vezes trabalhamos para nos divertir!

O Reddit é quase como um fórum com milhares de categorias diferentes. Com a sua conta, você pode navegar por assuntos técnicos, ver fotos de gatinhos, discutir questões de filosofia, aprender alguns life hacks e ficar por dentro das notícias do mundo todo!

Subreddits são como fóruns dentro do Reddit e as postagens são chamadas *threads*.

Para quem gosta de gatos, há o subreddit ["/r/cats"](https://www.reddit.com/r/cats) com threads contendo fotos de gatos fofinhos.
Para *threads* sobre o Brasil, vale a pena visitar ["/r/brazil"](https://www.reddit.com/r/brazil) ou ainda ["/r/worldnews"](https://www.reddit.com/r/worldnews/).
Um dos maiores subreddits é o "/r/AskReddit".

Cada *thread* possui uma pontuação que, simplificando, aumenta com "up votes" (tipo um like) e é reduzida com "down votes".

Sua missão é encontrar e listar as *threads* que estão bombando no Reddit naquele momento!
Consideramos como bombando *threads* com 5000 pontos ou mais.

### 1.1. Entrada

- Lista com nomes de subreddits separados por ponto-e-vírgula (`;`). Ex: "askreddit;worldnews;cats"

### 1.2. Parte 1

Gerar e imprimir uma lista contendo a pontuação, subreddit, título da thread, link para os comentários da thread e link da thread.
Essa parte pode ser um CLI simples, desde que a formatação da impressão fique legível.

### 1.3. Parte 2

Construir um robô que nos envie essa lista via Telegram sempre que receber o comando `/NadaPraFazer [+ Lista de subrredits]` (ex.: `/NadaPraFazer programming;dogs;brazil`)

## 2. Solução

### 2.1. Estrutura

Segue abaixo a estrura de arquivos utilizada.

```
crawlers/
|- crawler/ - Package python principal da solução
|  |- bot/ - Package para a parte 2 do desafio
|  |  |- __init__.py
|  |  |- __main__.py - Entry point do bot
|  |  |- decorators.py - Decorator utilizado para manipulação dos handlers
|  |  |- dispatcher.py - Core da solução do bot. Criação dos objetos da lib
|  |  |                  python-telegram-bot e configuração dos handlers
|  |  |- settings.py - Configurações do bot
|  |
|  |- cli/ - Package para a parte 1 do desafio
|  |  |- __init__.py
|  |  |- __main__.py - Entry point do cli
|  |
|  |- crawlers/
|  |  |- __init__.py
|  |  |- base.py - Crawler com funcionalidades básicas
|  |  |- functions.py - Funções auxiliares para obtenção de proxies e 
|  |  |                 user-agents
|  |  |- reddit.py - Implementação do crawler base para o reddit
|  |
|  |- __init__.py
|  |- enums.py - Enums utilizados em toda a solução
|  |- exceptions.py - Exceções utilizadas em toda a solução
|  |- funcitons.py - Funções utilizadas pelos entry points, tanto pelo cli,
|  |                 quanto pelo bot
|  |- logs.py - Configuração do sistema de logging e criação de loggers
|  |- parsers.py - Adaptação do ArgumentParser para a solução
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

Antes de executar qualquer uma das versões do programa, é necessária a ativação do **venv** do python.

```bash
. ./venv/bin/activate
```

**CLI**

A utilização básica do CLI é feita através de:

```bash
python -m crawler.cli subreddit # para apenas um subreddit
python -m crawler.cli 'subreddit1;subreddit2;...' # para múltiplos
```

Para maiores detalhes na utilização completa, execute

```bash
python -m crawler.cli -h
```

**BOT**

O bot é executado pelo comando:

```bash
python -m crawler.bot
```

> Nota: Para execução do bot, é necessário exportar a variável ambiente **TELEGRAM_BOT_TOKEN** com um token fornecido pelo BotFather (Telegram). Maiores detalhers, visite [BotFather](https://core.telegram.org/bots#6-botfather)

#### 2.2.3. Executando os testes unitários

Para a execução dos testes unitários, é necessário ter instalado as dependências de desenvolvimento. Vide seção [2.2.1. Instalando as dependências](#221-instalando-as-dependências).

Execute:

```bash
make tests
```

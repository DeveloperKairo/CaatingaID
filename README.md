# 🌵 CaatingaID

Sistema de catalogação e identificação inteligente de espécies botânicas do bioma Caatinga. Este projeto utiliza Programação Orientada a Objetos (POO) e Inteligência Artificial (Google Gemini) para auxiliar na identificação de plantas a partir de descrições em linguagem natural.

## 📸 Demonstração Visual

<div align="center">

<h3>1. Menu Principal</h3>
<img src="https://images2.imgbox.com/63/56/PRkQkJXN_o.png" width="600px">
<p><em>(Exemplo da tela inicial com as opções do sistema)</em></p>

<h3>2. Identificação com IA</h3>
<img src="https://images2.imgbox.com/f0/ff/u9cDspM7_o.png" width="600px">
<p><em>(Exemplo do Botânico Virtual analisando e dando dicas)</em></p>

</div>

</div>

---

## 📊 Diagrama de Classes

<div align="center">
<img src="https://images2.imgbox.com/c7/e3/6VV5v5Ma_o.png" width="700px">
<p><em>(Representação da arquitetura orientada a objetos do sistema)</em></p>
</div>

---

## 📂 Estrutura do Projeto

O projeto segue uma arquitetura modular organizada para facilitar a manutenção e escalabilidade:

- **`src/caatingaid/`**: Diretório principal do código fonte.
  - **`classes/`**: Núcleo do domínio (POO). Contém a classe mãe `Planta` e suas especializações (`Angiosperma`, `Gimnosperma`, etc.).
  - **`crud/`**: Camada de persistência. O `CrudPlantas` gerencia a leitura e escrita no arquivo JSON.
  - **`services/`**: Serviços externos. Aqui reside o `BotanicoAI`, que conecta o sistema ao Google Gemini.
  - **`main.py`**: O arquivo principal que gerencia o menu e o fluxo de interação com o usuário.
- **`banco_plantas.json`**: "Banco de dados" local onde o inventário é persistido.
- **`UML.png`**: Diagrama de classes do sistema.
- **`.env`**: (Não versionado) Arquivo de configuração onde fica sua `GOOGLE_API_KEY`.

---

## 🚀 Tecnologias Utilizadas

- **Linguagem**: Python 3.13+
- **Gerenciamento de Dependências**: [Poetry](https://python-poetry.org/)
- **Inteligência Artificial**: Google Gemini 2.5 Flash (via `google-generativeai`)
- **Persistência**: JSON (Armazenamento local em arquivo)
- **Variáveis de Ambiente**: `python-dotenv`

---

## 📋 Pré-requisitos e Instalação de Ferramentas

Antes de rodar o projeto, você precisa preparar seu computador. Siga o passo a passo abaixo:

### 1️⃣ Instalando o Python

Se você ainda não tem o Python instalado:

1.  Acesse o site oficial: [python.org/downloads](https://www.python.org/downloads/).
2.  Baixe a versão mais recente para Windows (3.13 ou superior).
3.  **⚠️ CRÍTICO:** Ao abrir o instalador, **marque a opção "Add Python to PATH"** na parte inferior da janela antes de clicar em "Install Now".
    - _Sem isso, o comando `python` não funcionará no seu terminal._

### 2️⃣ Instalando o Poetry

O Poetry é a ferramenta que organiza as bibliotecas do projeto.

1.  Abra seu terminal (PowerShell ou Prompt de Comando).
2.  Execute o comando simples via pip:
    ```bash
    pip install poetry
    ```
3.  Para verificar se instalou corretamente, digite `poetry --version`. Se aparecer um número de versão, está tudo pronto!

---

## ⚙️ Configuração do Ambiente (Obrigatório)

Para que a Inteligência Artificial funcione, você precisa configurar sua chave de acesso.

### 1. Criando a API Key

1.  Acesse o [Google AI Studio](https://aistudio.google.com/).
2.  Faça login e clique em "Get API key" para gerar sua chave secreta.

### 2. Criando o arquivo .env

O sistema busca por um arquivo chamado `.env` na **raiz do projeto** (`CaatingaID/`) para ler a chave com segurança.

1.  Na pasta do projeto, crie um arquivo novo chamado `.env` (exatamente assim, começa com ponto).
2.  Abra com o Bloco de Notas ou VS Code.
3.  Cole sua chave no seguinte formato:

```env
GOOGLE_API_KEY=Cole_Sua_Chave_Aqui_Sem_Aspas_Nem_Espaços
```

> **🔴 Erro Comum no Windows:** O Windows pode esconder a extensão do arquivo e salvá-lo como `.env.txt`.
>
> - **Solução:** No Explorador de Arquivos, vá em "Exibir" > "Mostrar" > Marque "Extensões de nomes de arquivos". Renomeie o arquivo apagando o `.txt` final se ele existir.

---

## 📦 Como Rodar o Projeto

Com tudo instalado e configurado, siga os passos para iniciar:

1.  **Abra o terminal** na pasta do projeto (`CaatingaID`).
2.  **Instale as dependências** do projeto (isso cria uma pasta virtual com tudo que o código precisa):
    ```bash
    poetry install
    ```
3.  **Execute o sistema**:
    ```bash
    poetry run python src/caatingaid/main.py
    ```

---

## 💾 Persistência de Dados

O sistema utiliza um banco de dados local simples e eficiente.

- **Arquivo:** `banco_plantas.json`
- **Funcionamento:**
  - Fica salvo na raiz do projeto.
  - Armazena todas as plantas cadastradas (Angiospermas, Gimnospermas, etc.).
  - É atualizado automaticamente a cada novo cadastro ou remoção.
  - Se você apagar este arquivo, perderá todos os cadastros feitos.

#Simulador de Arquitetura em Camadas (O Projeto Estrada)

Este é um simulador visual interativo construído em HTML, CSS e JavaScript puro que demonstra o fluxo de dados em uma arquitetura tradicional de quatro camadas (4-Tier Architecture): Apresentação, Negócio, Persistência e Banco de Dados.

O objetivo é visualizar de forma clara e animada o caminho que uma requisição (ida) e sua respectiva resposta (volta) percorrem através do sistema.

## Recursos em Destaque

- **Visualização de Fluxo:** A "Estrada" animada entre as camadas mostra o sentido da requisição (Downstream) e da resposta (Upstream).
- **Ícone de Pacote de Dados:** Um ícone (`📦` para ida e `✅` para volta) se move pela estrada, representando o tráfego de dados.
- **Logs Detalhados:** Um painel de logs registra o momento exato em que cada camada inicia seu processamento.
- **Simulação de Erro:** Se os dados de entrada (Nome ou CPF) forem inválidos, o fluxo é interrompido na Camada de Negócio (Camada 2) e retorna um erro 400 imediatamente.

## 🏗️ As Quatro Camadas

1.  **Apresentação (UI/Controller):** Captura a requisição do usuário.
2.  **Negócio (Service):** Aplica as regras de validação. Se falhar, interrompe o fluxo.
3.  **Persistência (Repository/DAL):** Prepara e envia o comando de I/O (Input/Output).
4.  **Banco de Dados (Database):** Armazenamento físico dos dados.

## 🚀 Como Visualizar

Este projeto é um único arquivo HTML e pode ser executado de duas formas:

### 1. Via GitHub Pages (Recomendado)

Acesse a demonstração online diretamente através do link do GitHub Pages (substitua `[SEU-USUARIO]` e `[SEU-REPO]`):
https://github.com/EngSivaldo/simulador-arquitetura-camadas

### 2. Localmente

1.  Clone este repositório:
    ```bash
    git clone [https://github.com/](https://github.com/)[SEU-USUARIO]/arquitetura-estrada-simulador.git
    ```
2.  Abra a pasta clonada e clique duas vezes no arquivo `index.html`. Ele será aberto no seu navegador.

## 💻 Como Usar o Simulador

1.  Preencha os campos **Nome** (mínimo 3 caracteres) e **CPF** (exatamente 11 dígitos numéricos).
2.  Clique em **Cadastrar Cliente**.
3.  Observe o painel de **Visualização do Fluxo de Camadas** e o **Logs de Fluxo** para acompanhar a jornada dos dados.

---

Feito com 💚 e JavaScript.

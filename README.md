# 🍕 Suporte do iFood — Aula de FastAPI e POO

Projeto desenvolvido durante uma aula de **Programação Orientada a Objetos (POO)**, com o objetivo de praticar conceitos básicos de desenvolvimento web utilizando **Python, FastAPI, HTML, CSS e JavaScript**.

A proposta foi criar uma página fictícia e bem-humorada de suporte do iFood, explorando a integração entre front-end e back-end e adicionando interatividade com JavaScript.

> ⚠️ **Aviso:** Este projeto possui fins exclusivamente educacionais e humorísticos. Não possui vínculo oficial com o iFood.

## 🚀 Funcionalidades

- ✅ Página web desenvolvida com HTML5.
- ✅ Estilização personalizada utilizando CSS3.
- ✅ Servidor web desenvolvido em Python com FastAPI.
- ✅ Botão interativo utilizando JavaScript.
- ✅ Exibição de mensagem humorística após clicar no botão.
- ✅ Animações e efeitos visuais em CSS.
- ✅ Layout responsivo para computadores e celulares.

### 🎮 Como funciona?

Ao acessar a página, o usuário encontra uma mensagem solicitando uma pizza.

Ao clicar no botão **"Pedir minha pizza 🍕"**, uma mensagem aparece na tela:

**💸 Você não tem dinheiro!**

*Hahaha pobre... 😂*

A mensagem é exibida dinamicamente utilizando JavaScript, sem necessidade de recarregar a página.

## 🛠️ Tecnologias utilizadas

| Tecnologia | Utilização |
|---|---|
| Python | Linguagem utilizada no back-end |
| FastAPI | Framework para criação do servidor web |
| HTML5 | Estrutura e conteúdo da página |
| CSS3 | Estilização, responsividade e animações |
| JavaScript | Interatividade e manipulação do DOM |
| Uvicorn | Servidor ASGI para executar o FastAPI |
| GitHub | Versionamento e armazenamento do projeto |

## 📂 Estrutura do projeto

```text
APIFAST_Aula_POO/
│
├── README.md
├── requirements.txt
│
└── aula-apifast/
    ├── main.py
    ├── index.html
    │
    └── static/
        └── style.css
```

Caso a versão estática tenha sido copiada para a raiz para publicação no GitHub Pages, também haverá um `index.html` e uma pasta `static/` na raiz do repositório.

## ⚙️ Como executar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/turi-pixel/APIFAST_Aula_POO.git
```

### 2. Acesse a pasta do projeto

```bash
cd APIFAST_Aula_POO/aula-apifast
```

### 3. Instale as dependências

Com Python instalado, execute:

```bash
python -m pip install -r ../requirements.txt
```

### 4. Inicie o servidor FastAPI

```bash
python -m uvicorn main:app --port 8080 --reload
```

### 5. Acesse o site

Abra seu navegador e acesse:

**http://127.0.0.1:8080**

O servidor carregará automaticamente a página HTML e seus arquivos CSS.

## 🌐 Demonstração online

A versão estática do projeto pode ser publicada gratuitamente utilizando GitHub Pages.

**Link previsto após a publicação:**

https://turi-pixel.github.io/APIFAST_Aula_POO/

> O link estará funcional somente depois que o GitHub Pages estiver configurado e a publicação for concluída.

## 📚 Conceitos praticados

Durante o desenvolvimento, foram trabalhados:

- Criação de rotas HTTP com FastAPI.
- Respostas HTML utilizando `HTMLResponse`.
- Disponibilização de arquivos estáticos com `StaticFiles`.
- Estruturação de páginas com HTML.
- Seletores, propriedades e animações CSS.
- Eventos de clique com JavaScript.
- Manipulação de elementos HTML pelo DOM.
- Organização de arquivos em projetos web.
- Publicação e versionamento com GitHub.

## 🔮 Possíveis melhorias

- [ ] Adicionar novas interações ao botão.
- [ ] Criar uma janela modal personalizada.
- [ ] Implementar novas rotas no FastAPI.
- [ ] Integrar requisições do JavaScript ao back-end.
- [ ] Melhorar o design e a experiência do usuário.

## 👨‍💻 Autor

**Victor Augusto**

Estudante de Engenharia de Software.

GitHub: [@turi-pixel](https://github.com/turi-pixel)

---

⭐ Projeto desenvolvido para fins de aprendizado, experimentação e diversão.
